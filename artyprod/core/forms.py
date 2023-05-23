from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
    
from django import forms
from .models import Project
  
class signup_form  (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class login_form(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'image', 'tags', 'service', 'status']

    