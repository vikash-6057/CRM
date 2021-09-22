from .models import *
from django.forms import ModelForm


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class UpdateOrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
