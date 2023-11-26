from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import Board_Model

def signup_func(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html')

        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています。'})

    return render(request, 'signup.html')


def login_func(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context': 'Logged in'})
        else:
            return render(request, 'login.html', {'context': 'Not Logged in'})
    return render(request, 'login.html', {'context': 'get method'})


def list_func(request):
    object_list = Board_Model.objects.all()
    return render(request, 'list.html', {'object_list': object_list})
