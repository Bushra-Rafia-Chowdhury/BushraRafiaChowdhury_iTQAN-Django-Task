from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import vegetables, fruits, beverages,babies, bread_bakery

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def vegetable(request):
    data = vegetables.objects.all()
    return render(request, 'vegetables.html', {'data': data})

def veg_detail(request, pk):
    data = vegetables.objects.get(pk=pk)
    return render(request,"veg_detail.html", {'data': data})


def fruit(request):
    data = fruits.objects.all()
    return render(request, 'fruit.html', {'data': data})

def fruit_detail(request, pk):
    data = fruits.objects.get(pk=pk)
    return render(request,"fruit_detail.html", {'data': data})


def beverage(request):
    data = beverages.objects.all()
    return render(request, 'beverage.html', {'data': data})

def beverage_detail(request, pk):
    data = beverages.objects.get(pk=pk)
    return render(request,"beverage_detail.html", {'data': data})



def baby(request):
    data = babies.objects.all()
    return render(request, 'baby.html', {'data': data})

def baby_detail(request, pk):
    data = babies.objects.get(pk=pk)
    return render(request,"baby_detail.html", {'data': data})


def bread(request):
    data = bread_bakery.objects.all()
    return render(request, 'bread_and_bakery.html', {'data': data})

def bread_detail(request, pk):
    data = bread_bakery.objects.get(pk=pk)
    return render(request,"bread_and_bakery_detail.html", {'data': data})