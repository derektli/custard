from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    def _unicode_(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie)
    def __unicode__(self):
        return self.name

