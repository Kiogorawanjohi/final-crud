from django.db import models


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    Names = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.CharField(max_length=10)
    National_ID = models.CharField(max_length=8)
    County = models.CharField(max_length=8)
    objects = models.Manager()

# Create your models here.
