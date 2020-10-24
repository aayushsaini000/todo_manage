from authapp.models import (User)
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:

        model = User
        fields = ('email', 'password','firstname','lastname','is_active', 'is_staff',
                    'is_superuser')

    def create(self, validated_data):
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        user = User.objects.create(email=email,password=make_password(password),**validated_data)

        return user

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

