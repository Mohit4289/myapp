from django import forms
from .models import Sign
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class SignRegistrationForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'address_line1', 'city', 'state', 'pincode']