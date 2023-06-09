from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [ 
         {'id': 1 ,'title':'Lets learn Python'},
         {'id': 2 ,'title':'Lets learn PHP'},
         {'id': 3 ,'title':'Lets learn NODE JS'},
         {'id': 4 ,'title':'Lets learn RUBY'},
]



def home(request):
    context={'rooms':rooms}
    return render(request ,'base/home.html',context)

def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context={'room':room}
    return render(request ,'base/room.html',context)