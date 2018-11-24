from django.shortcuts import render


# Basic View, using a Http Response, Request: It's what the client has sent to your server

def home(request):
    return render(request, 'home.html')
