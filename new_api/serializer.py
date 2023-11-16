from django.urls import path, include
from .models import User, Item, CustomerReview
from rest_framework import routers, serializers, viewsets


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = "__all__"
        

class ItemSerializer(serializers.ModelSerializer):
    review = CustomerReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'item_number', 'review']
        


        
class UserSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'mobile_number', 'user_number', 'items']
        

        
    def validate_mobile_number(self, value):
        if len(value) > 10 or not value.isdigit():
            raise serializers.ValidationError("Mobile number must be 10 digits or less.")
        return value
    def validate(self, data):
        if len(data['name'])==0:
            raise serializers.ValidationError("Name cannot be 0.")
        return data['name']
