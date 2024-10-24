from django.db import models

# Create your models here.
class Indices(models.Model):
    Nombre = models.CharField(max_length=50)
    Ticker = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Valor = models.IntegerField()
    Fecha_Actual = models.DateTimeField(auto_now_add=True)

