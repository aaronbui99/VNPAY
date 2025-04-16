import hashlib
import hmac
import urllib.parse
import datetime
import random
import string


class VnPay:
    def __init__(self):
        self.vnp_TmnCode = ""  # Terminal ID
        self.vnp_HashSecret = ""  # Secret key
        self.vnp_Url = ""  # Payment URL
        self.vnp_ReturnUrl = ""  # Return URL
        self.vnp_Version = "2.1.0"  # API version
        self.vnp_Command = "pay"  # Command
        self.vnp_CurrCode = "VND"  # Currency code
        self.vnp_Locale = "vn"  # Language
        self.requestData = {}  # Request data

    def get_payment_url(self, vnp_TxnRef, vnp_OrderInfo, vnp_OrderType, vnp_Amount, vnp_Locale, vnp_BankCode=None, vnp_IpAddr=None):
        """
        Build payment URL
        """
        # Set request data
        self.requestData = {
            "vnp_Version": self.vnp_Version,
            "vnp_Command": self.vnp_Command,
            "vnp_TmnCode": self.vnp_TmnCode,
            "vnp_Amount": int(vnp_Amount) * 100,  # Convert to VND (no decimal)
            "vnp_CurrCode": self.vnp_CurrCode,
            "vnp_TxnRef": vnp_TxnRef,
            "vnp_OrderInfo": vnp_OrderInfo,
            "vnp_OrderType": vnp_OrderType,
            "vnp_Locale": vnp_Locale,
            "vnp_ReturnUrl": self.vnp_ReturnUrl,
            "vnp_CreateDate": datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        }

        # Add IP address if provided
        if vnp_IpAddr:
            self.requestData["vnp_IpAddr"] = vnp_IpAddr

        # Add bank code if provided and not VNPAYQR (which is not supported in sandbox)
        if vnp_BankCode and vnp_BankCode != 'VNPAYQR':
            self.requestData["vnp_BankCode"] = vnp_BankCode

        # Add expiration date (15 minutes from now)
        expiration_date = datetime.datetime.now() + datetime.timedelta(minutes=15)
        self.requestData["vnp_ExpireDate"] = expiration_date.strftime('%Y%m%d%H%M%S')

        # Sort request data by key
        sorted_data = sorted(self.requestData.items())
        
        # Build hash data and query string
        hash_data = ""
        query = ""
        i = 0
        for key, value in sorted_data:
            if i == 0:
                hash_data += f"{key}={urllib.parse.quote_plus(str(value))}"
                query += f"{key}={urllib.parse.quote_plus(str(value))}"
            else:
                hash_data += f"&{key}={urllib.parse.quote_plus(str(value))}"
                query += f"&{key}={urllib.parse.quote_plus(str(value))}"
            i += 1

        # Create secure hash
        secure_hash = self.hmac_sha512(self.vnp_HashSecret, hash_data)
        query += f"&vnp_SecureHash={secure_hash}"
        
        # Return full payment URL
        return f"{self.vnp_Url}?{query}"

    def hmac_sha512(self, key, data):
        """
        Create HMAC-SHA512 signature
        """
        byteKey = key.encode('utf-8')
        byteData = data.encode('utf-8')
        return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()

    def validate_response(self, response_data):
        """
        Validate response data from VNPAY
        """
        # Get secure hash from response
        vnp_SecureHash = response_data.get('vnp_SecureHash', '')
        
        # Remove secure hash from data to verify
        if 'vnp_SecureHash' in response_data:
            response_data_copy = response_data.copy()
            response_data_copy.pop('vnp_SecureHash')
            
            # Sort data by key
            sorted_data = sorted(response_data_copy.items())
            
            # Build hash data
            hash_data = ""
            i = 0
            for key, value in sorted_data:
                if i == 0:
                    hash_data += f"{key}={urllib.parse.quote_plus(str(value))}"
                else:
                    hash_data += f"&{key}={urllib.parse.quote_plus(str(value))}"
                i += 1
            
            # Create secure hash
            calculated_hash = self.hmac_sha512(self.vnp_HashSecret, hash_data)
            
            # Compare hashes
            if vnp_SecureHash == calculated_hash:
                return True
        
        return False

    @staticmethod
    def get_client_ip(request):
        """
        Get client IP address from request
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    @staticmethod
    def generate_order_id():
        """
        Generate a unique order ID
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        random_str = ''.join(random.choices(string.digits, k=4))
        return f"{timestamp}{random_str}"