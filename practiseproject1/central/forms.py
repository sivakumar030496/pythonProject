from .models import central_works
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm


class centralForm(forms.ModelForm):
    class Meta:
        model= central_works
        fields='__all__'
