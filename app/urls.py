from django.urls import path
from .views import products, product_detail

urlpatterns = [
path('products/<int:pk>/', product_detail) ,
path('products/', products),
]
