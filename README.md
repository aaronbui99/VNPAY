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
7. Run the development server: `python manage.py runserver`

## Usage

- Access the admin interface at: `http://localhost:8000/admin/`
- View the items list at: `http://localhost:8000/`

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