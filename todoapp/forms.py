from django.forms import ModelForm
from .models import TodoList
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'is_done']


class CreateUserForm(UserCreationForm):
    fname = forms.CharField(max_length=20)
    lname = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['fname','lname','username','email','password1','password2']
