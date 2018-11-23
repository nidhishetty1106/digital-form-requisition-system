from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import  Student, faculty


class Userlogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class issueform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['subject','issue']
