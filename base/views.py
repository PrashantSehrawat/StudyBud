from django.shortcuts import render 
from django.http import HttpResponse 
from django.shortcuts import redirect
# Create your views here.
from .models import *
from django.db.models import Q
from base.form import CreateRoomForm
# rooms = [ 
#          {'id': 1 ,'title':'Lets learn Python'},
#          {'id': 2 ,'title':'Lets learn PHP'},
#          {'id': 3 ,'title':'Lets learn NODE JS'},
#          {'id': 4 ,'title':'Lets learn RUBY'},
# ]



def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)) 
    topic=Topic.objects.all()
    print(topic)
    context={'rooms':rooms,
             'topic':topic,
             }
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
    return render(request,'base/room_form.html',context)

def UpdateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=CreateRoomForm(instance=room) 
    if request.method == "POST":
     form=CreateRoomForm(request.POST,instance=room)
     if form.is_valid():
        form.save()
        return redirect("/")
    context={'form':form}
    return render(request,"base/room_form.html",context)

def DeleteRoom(request,pk):
   room=Room.objects.get(id=pk)
   room.delete()
   return redirect('/')
      


