from django.contrib import admin
from .models import Car, Make,Image, Message
# Register your models here.

admin.site.register(Car)
admin.site.register(Make)
admin.site.register(Image)
admin.site.register(Message)