
from django.db import models

# Create your models here.
class message(models.Model):
    ulevel = models.CharField(max_length=20, primary_key=True)
    uname = models.CharField(max_length=20)
    uaddr = models.CharField(max_length=20)
    ugrade = models.CharField(max_length=20)
class JDInfo(models.Model):
    title = models.CharField(max_length=50, default="", primary_key=True)
    price = models.URLField(max_length=10, default="")
    commit = models.URLField(max_length=10, default="")