from django.db import models

# Create your models here.
class details(models.Model):
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    url = models.CharField(max_length=500,unique = True)
    tag = models.CharField(max_length=50)
    videotype = models.CharField(max_length=15)
