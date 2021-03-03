from django.contrib import admin

from .models import Category, Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


