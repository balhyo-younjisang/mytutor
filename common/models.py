from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20, null=True)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True)
    isTutor = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    gender = models.TextField(default='male')
    introduce = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

