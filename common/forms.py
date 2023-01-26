from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    phone = forms.CharField(label="전화번호")
    gender = forms.IntegerField(label="성별")
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "phone", "gender"]
