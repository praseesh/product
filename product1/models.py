from django.db import models

class Product(models.Model):
    company = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.company


