from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegistrationForm(BaseUserCreationForm):

    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']