import uuid
from django.utils import timezone
from django.db import models
from authapp.managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.apps import apps



class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True,editable=False) 
    email = models.EmailField(
        unique=True,null=True, blank=True,
        error_messages={
            'unique': "User with this email already exists.",
        },
    )
    firstname = models.CharField(max_length=50,blank=True, null=True,default=None)
    lastname = models.CharField(max_length=50,blank=True, null=True,default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
