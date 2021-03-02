from django.shortcuts import render

from .models import Category, Product


def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'store.html', context)
