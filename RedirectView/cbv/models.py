from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=True)
