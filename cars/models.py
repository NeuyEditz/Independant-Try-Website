from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Make (models.Model):
    name=models.CharField(max_length=200)
    origin_country=models.CharField(max_length=150)
    founder=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    logo=models.ImageField(upload_to='media',height_field=None,width_field=None,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    


class Car (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    production_year = models.IntegerField()
    make = models.ForeignKey(Make,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Image (models.Model):
    photo=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100,null=True,blank=True)
    car_in=models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.url
    

class Message(models.Model):
    car_for=models.ForeignKey(Car, on_delete=models.CASCADE)
    host=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:70]