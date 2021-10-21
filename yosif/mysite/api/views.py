from django.shortcuts import render

# Create your views here.

from elsys.models import Car
from elsys.models import Board
from api.serializers import CarSerializer
from api.serializers import BoardSerializer
from django.http import JsonResponse
import requests

def cars_json(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return JsonResponse({'data': serializer.data }, safe=False)

def board_json(request):
    board = Board.objects.all()
    serializer = BoardSerializer(board, many = True)
    return JsonResponse({'data': serializer.data }, safe=False)

def table_json(request):
    r = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north').json()
    data = []
    for i in r['data']:
        time = i['attributes']['departure_time']
        status = i['attributes']['status']
        track = 'TBD'
        for j in r['included']:
            if j['id'] == i['relationships']['trip']['data']['id']:
                destination = j['attributes']['headsign']
        if i['relationships']['vehicle']['data'] is None:
            vehicle = 'None'
        else:
            for j in r['included']:
                if j['id'] == r['relationships']['vehicle']['data']['id']:
                    vehicle = r['attributes']['label']
        data.append({'time' : time, 'status' : status, 'track' : track, 'destination' : destination, 'vehicle' : vehicle})
    return data

