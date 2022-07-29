# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
#we will import the name of whatever model to be created. Custom user was just a sample


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email', 'first_name',  'last_name', 'years_of_programming_experience',) # new
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',  'last_name', 'years_of_programming_experience',) # new