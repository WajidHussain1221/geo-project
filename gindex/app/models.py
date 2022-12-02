from django.db import models

# Create your models here.


class Keyword(models.Model):
    word =  models.CharField(max_length=100)
    summary =  models.TextField()


class Term(models.Model):
    term = models.CharField(max_lenth =  100)