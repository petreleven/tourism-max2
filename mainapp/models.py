from django.db import models

# Create your models here.
class Players(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    image = models.ImageField()
class Movie(models.Model):
    name = models.CharField(max_length = 15)
    rate = models.IntegerField()
    descripiton=models.TextField()
class Song(models.Model):
    name = models.CharField(max_length = 100)
    artist = models.CharField(max_length= 100)
    description = models.TextField()
    lisener = models.IntegerField()