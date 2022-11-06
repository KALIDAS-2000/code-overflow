

from tkinter import Widget
from tkinter.tix import Select
from django import forms
from api.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from api.models import Questions

class RegistrationForm(UserCreationForm):
    class Meta():
        model=MyUser
        fields=["first_name","last_name","username","email",
        "phone","profile_pic","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class QuestionForm(forms.ModelForm):

    class Meta():
        model=Questions
        fields=[
            'discription','image',
        ]

        widgets={
            'discription':forms.Textarea(attrs={'class':"form-control bg-primary border border-success"}),
            'image':forms.FileInput(attrs={'class':'form-select bg-danger border border-success'}),
        }

class AnswerForm(forms.Form):
    answer=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control bg-success border border-danger'}))

