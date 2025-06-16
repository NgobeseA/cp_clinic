from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    office_number = models.CharField(max_length=10)