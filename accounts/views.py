from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import OrderFilter
# Create your views here.


def homeView(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = Order.objects.all().count()
    order_delivered = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'order_pending': order_pending, 'order_delivered': order_delivered}
    template_name = 'accounts/dashboard.html'
    return render(request, template_name, context)

def productView(request):
    template_name = 'accounts/products.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)


def customerView(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {'customer': customer, 'orders': orders,
               'total_orders': total_orders, 'myFilter': myFilter}
    template_name = 'accounts/customers.html'
    return render(request, template_name, context)


def createCustomerView(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    template_name = 'accounts/createCustomer.html'
    return render(request, template_name, context)


def createProductView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    template_name = 'accounts/createProduct.html'
    return render(request, template_name, context)


def updateOrderView(request, pk):
    order = Order.objects.get(id=pk)
    form = UpdateOrderForm(instance=order)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    template_name = 'accounts/updateOrder.html'
    return render(request, template_name, context)


def removeOrderView(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'order': order}
    template_name = 'accounts/removeOrder.html'
    return render(request, template_name, context)
