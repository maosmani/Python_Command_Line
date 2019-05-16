from django.db import models

class List(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

class Tutorials(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    author = models.CharField(max_length=150)
