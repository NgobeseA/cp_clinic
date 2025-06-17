from django.db import models
from patients.models import Patient
from doctor.models import Doctor

# Create your models here.
class ClinicBranch(models.Model):
    branch_name = models.CharField(max_length=50)
    unit_address = models.CharField(max_length=10)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()

class ConsultationRoom(models.Model):
    clinic_name = models.ForeignKey(ClinicBranch, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    building_floor = models.CharField(max_length=5)
    building_block = models.CharField(max_length=5)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    consultation_room = models.ForeignKey(ConsultationRoom, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    arrival_time = models.TimeField()

