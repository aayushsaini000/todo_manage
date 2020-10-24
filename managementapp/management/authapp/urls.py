from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path as url
from authapp import views


urlpatterns = [
    url('register', views.UserRegister.as_view()),
    url('login', views.UserAuth.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
