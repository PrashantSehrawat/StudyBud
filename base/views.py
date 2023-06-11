from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

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