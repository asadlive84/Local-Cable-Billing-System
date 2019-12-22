from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManger(UserManager):
    pass


class CustomUser(AbstractUser):

    full_name = models.CharField('Full Name', max_length=100)
    mobile_number = models.PositiveIntegerField('Mobile Number', unique=True)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['full_name', 'username', ]

    def __str__(self):
        return f"{self.full_name}"
