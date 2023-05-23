from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from core.models import *
from .forms import login_form, signup_form
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import ProjectForm
from .models import Project, Client


# Create your views here.
def index(request):            
    return render(request, 'core/index.html')


def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.user.email # use the email of the authenticated user
        send_mail(
            subject,
            message,
            from_email,
            ['ayoubmnafeg404@gmail.com'],
            fail_silently=False,
        )
        return redirect('contact')

    return render(request, 'core/contact.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services' : services})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'core/portfolio.html',{'projects': projects})

def filtered_portfolio(request, service):
    projects = Project.objects.filter(service__type=service)
    return render(request, 'core/portfolio.html', {'projects': projects})


def user_login(request):
    if request.method == 'POST':
        form = login_form(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = login_form()
    return render(request, 'core/login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()            
            client = Client.objects.create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = signup_form()
    return render(request, 'core/signup.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('index')

def team(request):
    staff = Staff.objects.all()
    return render(request, 'core/team.html', {'staff': staff})




@login_required
def profile(request):
    client = Client.objects.get(user=request.user)
    status = request.GET.get('status', '')
    # Retrieve the client's projects
    projects = Project.objects.filter(owner=client)

    context = {
        'client': client,
        'projects': projects,
        'status': status
    }
    
    return render(request, 'core/profile.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # Set the project owner to the current user
            project.owner = request.user
            project.save()
            form.save_m2m()  # Save the many-to-many field (tags in this case)
            return redirect('portfolio')
    else:
        form = ProjectForm()
    
    return render(request, 'core/add_project.html', {'form': form})