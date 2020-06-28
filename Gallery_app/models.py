from django.db import models

# Create your models here.
from Gallery_app import admin


class CCWorks(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=150)
    teacher = models.CharField(max_length=20)
    series = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    size = models.CharField(max_length=10)
    class Meta():
        abstract = True

class OilPaint(CCWorks):
    type = models.CharField(max_length=20)

class Video(CCWorks):
    type = models.CharField(max_length=20)

class threeDmodel(CCWorks):
    type = models.CharField(max_length=20)

class Poster(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=150)
    teacher = models.CharField(max_length=20)
    abstract = models.CharField(max_length=150)
    criticalWords = models.CharField(max_length=50)
    class Meta():
        abstract = True

class DSTposter(Poster):
    pass

class Admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    phonenum = models.CharField(max_length=11)
