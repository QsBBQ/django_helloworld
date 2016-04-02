from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    return render(request, "MenuTest/home.html")

def about(request):
    return render(request, "MenuTest/about.html")

def contact(request):
    return render(request, "MenuTest/contact.html")
