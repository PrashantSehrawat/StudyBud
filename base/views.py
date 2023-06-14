from django.shortcuts import render 
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import authenticate

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
    room_count=rooms.count()
    context={'rooms':rooms,
             'topic':topic,
             'room_count':room_count,}
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
      

def loginpage(request):
   
   if request.method=="POST":
      username=request.POST.get('username')
      password=request.POST.get('password')
      try:
        user=User.objects.get(username=username)
      except:
          messages.error(request, "Username Does Not Exists")
          
      user = authenticate(request,username=username, password=password)

      if user is not None:
         login(request,user)
         return redirect("/")
      else:
         messages.error(request, "Username Or Password Does Not Match")
   context={}
   return render(request,"base/login_register.html",context)
