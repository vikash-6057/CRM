from django.db import models

# Create your models here.


class Customer(models.Model):

    # id = models.BigAutoField(primary_key=True) it's added  by default
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(help_text='abc@xyz.com', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('InDoor', 'InDoor'),
        ('OutDoor', 'OutDoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# class Order(models.Model):

#     # customer =
#     # product =
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
