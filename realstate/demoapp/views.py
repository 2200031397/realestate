from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PropertyInformationForm
from .models import User, PropertyInformation


def home(request):
    return render(request,"home.html")


def checklogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = User.objects.filter(Q(Username=uname) & Q(password=pwd))

    if flag:
        return render(request, "mainpage.html")
    else:
        return HttpResponse("Login Failed")

def insertsite(request):
    if request.method == 'POST':
        form = PropertyInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success_page')  # Redirect to a success page
    else:
        form = PropertyInformationForm()
    return render(request, 'insertsite.html', {'form': form})

def display_property_information(request):
    property_entries = PropertyInformation.objects.all()
    return render(request, 'display_property.html', {'property_entries': property_entries})

def firstpage(request):
    return render(request,'first.html')

def signup(request):
    return render(request,'signup.html')

def registeruser(request):
    if request.method=="POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]

        user=User(Username=uname, password=pwd)
        User.save(user)
        return HttpResponse("enrolled successfully")

