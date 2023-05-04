from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def login(request):
    return render(request, 'core/login.html')

def signin(request):
    return render(request, 'core/signin.html')