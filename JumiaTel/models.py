from django.db import models

class Smartphone(models.Model):
    name = models.CharField(max_length=100)
    lien = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
