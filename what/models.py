from time import time
from django.db import models

# Create your models here.
class What(models.Model):
    event = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField(max_length=8)
    location = models.CharField(max_length=100)
    
class Past(models.Model):
    pastevent = models.CharField(max_length=100)
    pastdescription = models.CharField(max_length=300)
    pastdate = models.DateField(max_length=8)
    pastlocation = models.CharField(max_length=100)

class Deals(models.Model):
    place = models.CharField(max_length=100)
    deal = models.CharField(max_length=300)
    previousprice = models.IntegerField(8)
    duration = models.DateTimeField(100)
    
class Sites(models.Model):
    place = models.CharField(max_length=200)
    history = models.CharField(max_length=300)
    whattosee = models.CharField(max_length=300)