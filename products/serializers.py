from rest_framework.serializers import ModelSerializer
from .models import Product


from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo", "create_at"]
