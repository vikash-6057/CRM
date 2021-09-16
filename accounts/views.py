from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homeView(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)
