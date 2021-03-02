from django.contrib import admin

from .models import Category, Customer, Product

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
