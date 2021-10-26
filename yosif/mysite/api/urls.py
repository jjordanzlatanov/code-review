from django.urls import include, path
from api import views

urlpatterns = [
    path('cars', views.cars_json),
    path('board', views.board_json),
    path('table', views.table_json),
]
