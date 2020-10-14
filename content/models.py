from django.db import models

# Create your models here.
class newsList(models.Model):
    site = models.CharField(max_length=20)
    header = models.CharField(max_length=20)
    url = models.CharField(max_length=30)




