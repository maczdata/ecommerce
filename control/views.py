from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render (request, 'control/login.html')


def signup(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'control/signup.html', {'form':form})


