from rest_framework import serializers
from .models import Car
from .models import Board


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'color', 'brand', 'description', 'made']

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'carrier', 'time', 'destination', 'trainNumber', 'status']