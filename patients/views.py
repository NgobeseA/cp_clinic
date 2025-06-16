from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'patients/home.html')

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,'Please make sure')
    return render(request, 'patients/signup.html', {'form': form})

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request, 'patients/home.html')
        else:
            messages.error("Incorrect username or password!!!")
    else:
        form = authenticate()
    return render(request, 'patients/login.html', {'form': form})
    