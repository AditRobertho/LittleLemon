from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    model = Booking
    fields = '__all__'
    permissions_classes = [permissions.IsAuthenticated]