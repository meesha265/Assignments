from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    First_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=40)
    Age = models.IntegerField()

    def __str__(self):
        return self.First_name

class Song(models.Model):
    Title = models.CharField(max_length=80)
    Date_released = models.DateField(default=datetime.today)
    Likes = models.IntegerField()
    Artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.Title

class Lyric(models.Model):
    Content = models.CharField(max_length=10000)
    Song_id = models.ForeignKey( Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.Content