from django.contrib import admin
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('room/<str:pk>',room,name="room"),
    path('create_room/',CreateRoom,name="Create-Room"),
]
