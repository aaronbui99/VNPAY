"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import payment_return, payment_ipn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # Add direct paths for VNPAY return and IPN
    path('payment_return', payment_return, name='payment_return'),
    path('payment_ipn', payment_ipn, name='payment_ipn'),
]
