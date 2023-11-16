from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, ItemSerializer, CustomerReviewSerializer
from .models import User, Item,CustomerReview

class user_list(APIView):
    
    def get(self, request, format=None):
        items = User.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class item_list(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_details(APIView):
    def get(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class item_details(APIView):
    def get(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CustomerReviewList(APIView):
    def get(self, request, format=None):
        reviews = CustomerReview.objects.all()
        serializer = CustomerReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerReviewDetail(APIView):
    def get(self, request, pk, format=None):
        review = get_object_or_404(CustomerReview, pk=pk)
        serializer = CustomerReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = get_object_or_404(CustomerReview, pk=pk)
        serializer = CustomerReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = get_object_or_404(CustomerReview, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)