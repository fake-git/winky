from django.forms import *
from django import forms


class RegisterForm(Form):

    first_name = forms.CharField(max_length=60, required=True, widget=TextInput)
    last_name = forms.CharField(max_length=60, required=True, widget=TextInput)
    email = forms.EmailField(widget=EmailInput)
    password = forms.CharField(required=True, widget=PasswordInput)


class LoginForm(Form):
    email = forms.EmailField(widget=EmailInput)
    password = forms.CharField(required=True, widget=PasswordInput)