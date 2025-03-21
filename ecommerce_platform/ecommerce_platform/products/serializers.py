# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']

class AddProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ['name', 'category', 'price', 'description', 'image']

class GetProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ['id', 'name', 'category', 'price', 'description', 'image', 'created_at']