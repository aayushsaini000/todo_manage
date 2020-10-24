from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from authapp.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authapp.serializers import (UserRegisterSerializer)
from authapp.authentication import CustomAuthentication
from django.contrib.auth.hashers import make_password




# Create your views here.
class UserRegister(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                email = str(user)
                return Response(
                    {
                        "token": token.key,
                        "error": False
                    },
                    status=status.HTTP_201_CREATED)
        else:
            data = {"error": True, "errors": serializer.errors}

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserAuth(APIView):
    def post(self, request):
        email = None
        if 'email' in request.data:
            if request.data['email'] != "":
                email = request.data['email']
            else:
                pass
        # if email is not None:
        user = CustomAuthentication().authenticate(
            email=email, password=request.data.get("password"))
        # else:
        #     user = CustomAuthentication().authenticate(email=email,phone=phone,password=request.data.get("password"))
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except:
                token = Token.objects.create(user=user)
            return Response({"token": token.key, "error": False})
        else:
            data = {
                "error": True,
                "msg": "User does not exist or password is wrong"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
