from django.db import models
from patients.models import Patient
from doctor.models import Doctor

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    consultation_room = models.ForeignKey(ConsultationRoom, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    arrival_time = models.TimeField()

class ConsultationRoom(models.Model):
    clinic_name = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    building_floor = models.CharField(max_length=5)
    building_block = models.CharField(max_length=5)