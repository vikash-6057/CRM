from django.urls import path
from .views import *
urlpatterns = [
    path('', homeView, name='home'),
    path('products/', productView, name='products'),
    path('customer/<int:pk>/', customerView, name='customer'),
    path('create_customer/', createCustomerView, name='createCustomer'),
    path('create_product/', createProductView, name='createProduct'),
    path('update_order/<int:pk>/', updateOrderView, name='updateOrder'),
    path('remove_order/<int:pk>/', removeOrderView, name='removeOrder'),
]
