from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

from django.urls import path

def home(request):
    return HttpResponse("Hello World")


def profile(request):
    return HttpResponse("Hello Profile")

def settings(request):
    return HttpResponse("Hello Settings")

def about(request):
    return render(request, 'about.html')

