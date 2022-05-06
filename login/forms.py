#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Creating fields for the forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email address'}),
            #'password1': forms.TextInput(attrs={'class': 'form-control'}),
            #'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }