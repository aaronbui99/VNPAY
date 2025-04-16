from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

# Temporarily comment out the Item model import
# from .models import Item
from .vnpay import VnPay

# Add a view for payment documentation
def payment_docs(request):
    """
    Display payment documentation
    """
    return render(request, 'myapp/payment_docs.html')

# Create your views here.
def index(request):
    # Temporarily use dummy data instead of database query
    items = [
        {'id': 1, 'name': 'Item 1', 'description': 'Description for Item 1'},
        {'id': 2, 'name': 'Item 2', 'description': 'Description for Item 2'},
        {'id': 3, 'name': 'Item 3', 'description': 'Description for Item 3'},
    ]
    context = {'items': items}
    return render(request, 'myapp/index.html', context)

def item_detail(request, item_id):
    # Temporarily use dummy data instead of database query
    item = {
        'id': item_id,
        'name': f'Item {item_id}',
        'description': f'Description for Item {item_id}',
        'created_at': timezone.now(),
        'updated_at': timezone.now(),
    }
    context = {'item': item}
    return render(request, 'myapp/item_detail.html', context)

def payment(request):
    """
    Display payment form
    """
    # Generate a unique order ID
    order_id = VnPay.generate_order_id()
    
    context = {
        'order_id': order_id,
    }
    return render(request, 'myapp/payment.html', context)

def create_payment(request):
    """
    Create payment URL and redirect to VNPAY
    """
    if request.method != 'POST':
        return redirect('myapp:payment')
    
    # Get form data
    order_id = request.POST.get('order_id')
    amount = int(request.POST.get('amount', 10000))
    order_desc = request.POST.get('order_desc', 'Payment for order')
    bank_code = request.POST.get('bank_code', '')
    language = request.POST.get('language', 'vn')
    order_type = request.POST.get('order_type', 'billpayment')
    
    # Remove VNPAYQR if selected (not supported in sandbox)
    if bank_code == 'VNPAYQR':
        bank_code = ''  # Let VNPAY show the payment method selection screen
    
    # Initialize VNPAY
    vnpay = VnPay()
    vnpay.vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnpay.vnp_HashSecret = settings.VNPAY_HASH_SECRET_KEY
    vnpay.vnp_Url = settings.VNPAY_PAYMENT_URL
    vnpay.vnp_ReturnUrl = settings.VNPAY_RETURN_URL
    
    # Get client IP
    ip_addr = VnPay.get_client_ip(request)
    
    # Create payment URL with current timestamp to ensure uniqueness
    import time
    txn_ref = f"{order_id}_{int(time.time())}"
    
    # Create payment URL
    payment_url = vnpay.get_payment_url(
        vnp_TxnRef=txn_ref,
        vnp_OrderInfo=order_desc,
        vnp_OrderType=order_type,
        vnp_Amount=amount,
        vnp_Locale=language,
        vnp_BankCode=bank_code,
        vnp_IpAddr=ip_addr
    )
    
    # For debugging
    print(f"Payment URL: {payment_url}")
    
    # Redirect to payment URL
    return redirect(payment_url)

@csrf_exempt
def payment_return(request):
    """
    Handle payment return from VNPAY
    """
    # Initialize VNPAY
    vnpay = VnPay()
    vnpay.vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnpay.vnp_HashSecret = settings.VNPAY_HASH_SECRET_KEY
    
    # Get all data from VNPAY
    response_data = request.GET.dict()
    
    # Validate response data
    is_valid = vnpay.validate_response(response_data)
    
    # Get payment result
    vnp_ResponseCode = response_data.get('vnp_ResponseCode', '')
    vnp_TransactionStatus = response_data.get('vnp_TransactionStatus', '')
    
    # Check if payment is successful
    payment_success = is_valid and vnp_ResponseCode == '00' and vnp_TransactionStatus == '00'
    
    # Format amount
    amount = int(response_data.get('vnp_Amount', 0)) / 100  # Convert back from VND (no decimal)
    
    # Format transaction date
    transaction_date = ''
    if 'vnp_PayDate' in response_data:
        try:
            pay_date = response_data.get('vnp_PayDate', '')
            if pay_date:
                date_obj = datetime.datetime.strptime(pay_date, '%Y%m%d%H%M%S')
                transaction_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
    
    # Prepare context
    context = {
        'payment_success': payment_success,
        'error_message': 'Payment failed. Please try again.' if not payment_success else '',
        'order_id': response_data.get('vnp_TxnRef', ''),
        'amount': amount,
        'transaction_date': transaction_date,
        'transaction_no': response_data.get('vnp_TransactionNo', ''),
        'bank_code': response_data.get('vnp_BankCode', ''),
        'card_type': response_data.get('vnp_CardType', ''),
        'order_info': response_data.get('vnp_OrderInfo', ''),
    }
    
    return render(request, 'myapp/payment_return.html', context)

@csrf_exempt
def payment_ipn(request):
    """
    Handle IPN (Instant Payment Notification) from VNPAY
    """
    # Initialize VNPAY
    vnpay = VnPay()
    vnpay.vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnpay.vnp_HashSecret = settings.VNPAY_HASH_SECRET_KEY
    
    # Get all data from VNPAY
    response_data = request.GET.dict()
    
    # Validate response data
    is_valid = vnpay.validate_response(response_data)
    
    # Get payment result
    vnp_ResponseCode = response_data.get('vnp_ResponseCode', '')
    vnp_TransactionStatus = response_data.get('vnp_TransactionStatus', '')
    
    # Check if payment is successful
    payment_success = is_valid and vnp_ResponseCode == '00' and vnp_TransactionStatus == '00'
    
    # Process payment result
    if payment_success:
        # TODO: Update order status in database
        # For example:
        # order_id = response_data.get('vnp_TxnRef', '')
        # amount = int(response_data.get('vnp_Amount', 0)) / 100
        # transaction_no = response_data.get('vnp_TransactionNo', '')
        # Update order status in database
        
        # Return success response to VNPAY
        return JsonResponse({
            'RspCode': '00',
            'Message': 'Confirm Success'
        })
    else:
        # Return error response to VNPAY
        return JsonResponse({
            'RspCode': '99',
            'Message': 'Confirm Fail'
        })
