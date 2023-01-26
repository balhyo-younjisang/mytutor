from django.urls import path, include
from . import views
from common import models


app_name = 'home'

urlpatterns = [
    path('', views.index),
]