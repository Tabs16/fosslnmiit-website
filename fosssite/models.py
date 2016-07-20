from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	email=models.ForeignKey('auth.User')
	password=models.CharField(max_length=200)
