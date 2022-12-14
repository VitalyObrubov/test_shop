from django.contrib import admin
from app.models import Product

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'price', 'status']
    list_display_links = ['title', 'sku', 'price', 'status']