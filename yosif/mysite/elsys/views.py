from django.shortcuts import render
from api import views

# Create your views here.
PI = 3.14

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def board(request):
    return render(request, 'board.html')

def table(request):
    table = views.table_json(request)
    return render(request, 'table.html', {'content': table})