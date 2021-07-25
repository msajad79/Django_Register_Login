from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=256)

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput())

    

