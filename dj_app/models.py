from django.db import models

# Create your models here.

class Users(models.Model):
    user_id=models.CharField(max_length=50)
    password=models.CharField(max_length=30)