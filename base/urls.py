from django.contrib import admin
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('room/<str:pk>',room,name="room"),
    path('create_room/',CreateRoom,name="Create-Room"),
    path('update_room/<str:pk>',UpdateRoom,name="Update-Room"),
    path('delete_room/<str:pk>',DeleteRoom,name="Delete-Room"),

    # AUTHETICATION URLS
    path('login/',loginpage,name="User-login"),
    path('logout/',UserLogOut,name="User-logout"),
    
]
