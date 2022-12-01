from django.db import models
from datetime import datetime

# Create your models here.
class ROOM(models.Model):
    name = models.CharField(max_length=1000)
class message(models.Model):
    value =models.CharField(max_length=10000)
    date =models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)