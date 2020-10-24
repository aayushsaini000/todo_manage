from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path as url
from tasks import views


urlpatterns = [
    url('task', views.CreateTasks.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
