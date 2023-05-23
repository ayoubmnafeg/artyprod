from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
  
class signup_form  (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class login_form(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    