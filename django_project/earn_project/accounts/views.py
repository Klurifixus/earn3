from django.shortcuts import render

def forum(request):
    # Your view logic here
    return render(request, 'templates/login.html')

def register(request):
    # Your view logic here
    return render(request, 'registration/register.html')