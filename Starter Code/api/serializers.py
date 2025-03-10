from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product 
        fields = (
            'id',
            'name',
            'description',
            'stock',
            'price'
        )
    def validate_price(self , value) :
        if value <= 0 :
            raise serializers.ValidationError(
                "Price must be more than 0"
            )
        return value 