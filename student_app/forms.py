from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'roll_number', 'email', 'profile_image', 'password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'roll_number', 'email', 'profile_image']