from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, email, password, password2)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User name already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
