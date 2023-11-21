from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Car,Make,Image,Message
import django.contrib.auth.views
from .forms import UserRegistrationForm  
from django.urls import reverse
# Create your views here.


def home(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''

    cars=Car.objects.filter(
        Q(make__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
    )
    makes=Make.objects.all()
    car_count=cars.count()
    context={'cars':cars,'makes':makes,'car_count':car_count}
    return render(request,'cars/home.html',context)


def CarPageView (request,pk):
    car=Car.objects.get(id=pk)
    car_images=car.image_set.all()
    chat=car.message_set.all().order_by('created')

    if request.method =="POST":
        message=Message.objects.create(
            car_for=car,
            host=request.user,
            body=request.POST.get('body'),
         )
    context={'car':car,'car_images':car_images,'chat':chat.select_related('host')}
    return render(request, 'cars/car-shablon.html',context)

def RegistrationView (request):
    form=UserRegistrationForm(request.POST or None)
    if form.is_valid() and request.method=='POST':
        form.save()
        return HttpResponseRedirect(reverse('home', args=()))
    context={'form':form}
    return render(request,'cars/register.html',context)