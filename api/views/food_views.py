from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.food import Food
from ..serializers import FoodSerializer, UserSerializer

# Create your views here.
class Foods(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        # foods = Food.objects.all()
        foods = Food.objects.filter(owner=request.user.id)
        data = FoodSerializer(foods, many=True).data
        return Response(data)

    serializer_class = FoodSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['food']['owner'] = request.user.id
        # Serialize/create food
        food = FoodSerializer(data=request.data['food'])
        if food.is_valid():
            m = food.save() # maybe switch 'm' to 'f'
            return Response(food.data, status=status.HTTP_201_CREATED)
        else:
            return Response(food.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        food = get_object_or_404(Food, pk=pk)
        data = FoodSerializer(food).data
        # Only want to show owned foods?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this food')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        food = get_object_or_404(Food, pk=pk)
        if not request.user.id == food.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this food')
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['food'].get('owner', False):
            del request.data['food']['owner']

        # Locate Food
        food = get_object_or_404(Food, pk=pk)
        # Check if user is  the same
        if not request.user.id == food.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this food')

        # Add owner to data object now that we know this user owns the resource
        request.data['food']['owner'] = request.user.id
        # Validate updates with serializer
        ms = FoodSerializer(food, data=request.data['food'])
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
