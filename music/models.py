from django.db import models

# Create your models here.

class Music(models.Model): 
    title = models.CharField()
    artist = models.CharField()
    album = models.CharField()
    release_date = models.DateField()
    genre = models.CharField()