from rest_framework import serializers
from app.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'sku', 'price', 'status', 'image')
