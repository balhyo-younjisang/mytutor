from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            phone=request.POST['phone'],
                                            gender=request.POST['gender'],
                                            isTutor=False,
                                            )
            login(request, user)
            return redirect('/')
        return render(request, 'common/signup.html')
    return render(request, 'common/signup.html')


def signup_tutor(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            phone=request.POST['phone'],
                                            gender=request.POST['gender'],
                                            isTutor=True,
                                            )
            login(request, user)
            return redirect('/')
        return render(request, 'common/signup_tutor.html')
    return render(request, 'common/signup_tutor.html')


def profile(request, params):
    return render(request, 'common/profile.html')


