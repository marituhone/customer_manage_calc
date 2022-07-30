from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class Task(models.Model):   
   
    name =  models.CharField(max_length=255 ,null =True)
    description =  models.TextField()
    is_deleted = models.BooleanField(default=False)
   
    def __str__ (self):
        return self.username