from django.urls import path

from .views import *

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
]

