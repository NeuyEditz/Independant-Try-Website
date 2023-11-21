from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.views  


urlpatterns = [
    path ('car-page/<str:pk>/', views.CarPageView , name='car-page'),
    path ('', views.home , name='home'),
    path ('login/', django.contrib.auth.views.LoginView.as_view(template_name='cars/login.html'), name='login'),
    path ('logout/', django.contrib.auth.views.LogoutView.as_view(template_name='cars/logout.html'), name='logout'),
    path ('register/', views.RegistrationView , name='register'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  