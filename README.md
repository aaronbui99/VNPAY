# My Django Project

A simple Django application for managing items.

## Features

- View a list of items
- View item details
- Admin interface for managing items

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin123`
7. Run the development server: `python manage.py runserver`

## Usage

- Access the admin interface at: `http://localhost:8000/admin/`
  - Username: `admin`
  - Password: `admin123`
- View the items list at: `http://localhost:8000/`
- Access the payment page at: `http://localhost:8000/payment/`
- View payment documentation at: `http://localhost:8000/payment-docs/`

## VNPAY Test Card Information

Below are test cards that can be used with the VNPAY sandbox environment:

### Test Card Table (from VNPAY Sandbox)

| # | Thông tin thẻ | Ghi chú |
| --- | --- | --- |
| 1 | Ngân hàng: `NCB`<br>Số thẻ: `9704198526191432198`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`07/15`<br>Mật khẩu OTP:`123456` | Thành công |
| 2 | Ngân hàng: `NCB`<br>Số thẻ: `9704195798459170488`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`07/15` | Thẻ không đủ số dư |
| 3 | Ngân hàng: `NCB`<br>Số thẻ: `9704192181368742`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`07/15` | Thẻ chưa kích hoạt |
| 4 | Ngân hàng: `NCB`<br>Số thẻ: `9704193370791314`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`07/15` | Thẻ bị khóa |
| 5 | Ngân hàng: `NCB`<br>Số thẻ: `9704194841945513`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`07/15` | Thẻ bị hết hạn |
| 6 | Loại thẻ quốc tế: `VISA (No 3DS)`<br>Số thẻ: `4456530000001005`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/26`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 7 | Loại thẻ quốc tế: `VISA (3DS)`<br>Số thẻ: `4456530000001096`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/26`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 8 | Loại thẻ quốc tế: `MasterCard (No 3DS)`<br>Số thẻ: `5200000000001005`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/26`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 9 | Loại thẻ quốc tế: `MasterCard (3DS)`<br>Số thẻ: `5200000000001096`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/26`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 10 | Loại thẻ quốc tế: `JCB (No 3DS)`<br>Số thẻ: `3337000000000008`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/26`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 11 | Loại thẻ quốc tế: `JCB (3DS)`<br>Số thẻ: `3337000000200004`<br>CVC/CVV: `123`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`12/24`<br>Email:`test@gmail.com`<br>Địa chỉ:`22 Lang Ha`<br>Thành phố:`Ha Noi` | Thành công |
| 12 | Loại thẻ ATM nội địa: `Nhóm Bank qua NAPAS`<br>Số thẻ: `9704000000000018`<br>Số thẻ: `9704020000000016`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày phát hành:`03/07`<br>OTP:`otp` | Thành công |
| 13 | Loại thẻ ATM nội địa: `EXIMBANK`<br>Số thẻ: `9704310005819191`<br>Tên chủ thẻ:`NGUYEN VAN A`<br>Ngày hết hạn:`10/26` | Thành công |

**Ghi chú:** Trên môi trường test (thử nghiệm) chỉ sử dụng được các thông tin thẻ theo danh sách trên. Các Ngân hàng khác do kết nối đã lâu nên môi trường test đã bị tạm đóng.

## Project Structure

```
myproject/
├── myapp/                  # Main application
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── myproject/              # Project settings
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL routing
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.