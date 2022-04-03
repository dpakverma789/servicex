from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100, unique=True)
    customer_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.firstname
