from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    avatar = models.FileField(upload_to='avatar/')
