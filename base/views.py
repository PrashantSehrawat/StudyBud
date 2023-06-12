from django.shortcuts import render 
from django.http import HttpResponse 
from django.shortcuts import redirect
# Create your views here.
from .models import *

from base.form import CreateRoomForm
# rooms = [ 
#          {'id': 1 ,'title':'Lets learn Python'},
#          {'id': 2 ,'title':'Lets learn PHP'},
#          {'id': 3 ,'title':'Lets learn NODE JS'},
#          {'id': 4 ,'title':'Lets learn RUBY'},
# ]



def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request ,'base/home.html',context)

def room(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
    return render(request ,'base/room.html',context)

def CreateRoom(request):
    form=CreateRoomForm()
    if request.method == "POST":
          print(request.POST)
          form=CreateRoomForm(request.POST)
          if form.is_valid():
           form.save()
           return redirect("/")
    context={'form':form}
    return render(request,'base/create_room.html',context)
