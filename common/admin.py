from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# from .models import Tutor

# Register your models here.
admin.site.register(User, UserAdmin)
