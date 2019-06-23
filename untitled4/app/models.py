from django.db import models
models.CharField()
# Create your models here.

class User(models.Model):
    user=models.CharField(max_length = 32)
    pwd=models.CharField(max_length = 32)

    #def _str_(self):
    #    return self.user + self.pwd

class Img(models.Model):
    path = models.CharField(max_length=128)
