from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('payment/', views.payment, name='payment'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment-return/', views.payment_return, name='payment_return'),
    path('payment-ipn/', views.payment_ipn, name='payment_ipn'),
    path('payment-docs/', views.payment_docs, name='payment_docs'),
]