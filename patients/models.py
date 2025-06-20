from django.db import models


# Create your models here.
class Cities(models.Model):
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)

class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    unit_number = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    province = models.ForeignKey(Cities, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=200)
    registered_date = models.DateTimeField(auto_now_add=True)

