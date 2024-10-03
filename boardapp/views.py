from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Board_Model
from django.contrib.auth.decorators import login_required


def signup_func(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html')

        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録済みです。'})

    return render(request, 'signup.html')


def login_func(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})

    # ここではgetの場合
    return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return redirect('login')

@login_required
def list_func(request):
    object_list = Board_Model.objects.all()
    return render(request, 'list.html', {'object_list': object_list})
