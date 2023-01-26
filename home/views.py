from django.shortcuts import render
from django.http import HttpResponse
from common import models


def index(request):
    return render(request, 'home/home.html')


