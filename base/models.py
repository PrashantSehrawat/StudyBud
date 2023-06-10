from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    topic=models.CharField(max_length=200)

    def __str__(self):
        return self.topic

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL , null=True) 
    name=models.CharField(max_length=20)
    Topic=models.ForeignKey(Topic ,on_delete=models.CASCADE,null=True)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room ,on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]