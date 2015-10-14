from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello everybody! Click <a href="/rango/about/">here</a> to visit the about page.')

def about(request):
    return HttpResponse("This is where the 'About' page will go! Return to the <a href='/rango/'>home page</a>.")
