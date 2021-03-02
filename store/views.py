from django.shortcuts import render

from .models import Customer, Category, Product, Order, OrderItem


def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

