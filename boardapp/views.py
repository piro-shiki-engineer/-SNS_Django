from django.shortcuts import render


def signup_func(request):
    return render(request, 'signup.html', {})
