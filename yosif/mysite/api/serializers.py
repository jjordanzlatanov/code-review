from rest_framework import serializers
from elsys.models import Car
from elsys.models import Board


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'color', 'brand', 'description', 'made']

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'carrier', 'time', 'destination', 'trainNumber', 'status']
