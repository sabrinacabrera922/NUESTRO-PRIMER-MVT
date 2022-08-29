from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=60)
    telefono = models.FloatField()
    fecha_nacimiento = models.DateField()