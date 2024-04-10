from django.db import models

# Create your models here.

class MesTrains(models.Model) : 
    trainId = models.AutoField(primary_key=True)
    nom = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 10)
    heures = models.CharField(max_length = 100)


