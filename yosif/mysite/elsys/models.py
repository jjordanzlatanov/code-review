from django.db import models

# Create your models here.

class Car(models.Model):
    color = models.CharField(max_length=100)
    made = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    description = models.TextField()

class Board(models.Model):
    carrier = models.CharField(max_length=100)
    time = models.DateTimeField()
    destination = models.CharField(max_length=100)
    trainNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=100)