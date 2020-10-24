from django.db import models
from authapp.models import User
from django.utils import timezone


# Create your models here.
class Tasks(models.Model):
    id = models.AutoField(primary_key=True,editable=False) 
    user = models.ForeignKey(User,
                             related_name='User',
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE)
    task_name = models.CharField(max_length=350)
    description = models.CharField(max_length=8000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField('start_date',
                                    default=timezone.now,
                                    blank=True)
    end_date = models.DateTimeField('end_date',
                                    default=timezone.now,
                                    blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
