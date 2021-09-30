# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Electeur(models.Model):
    id_electeur = models.CharField(max_length=200)
    token = models.CharField(max_length=10)
    a_vote = models.BooleanField(default=False)


class Candidat(models.Model):
    id_candidat = models.IntegerField(default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    parti = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class Block(models.Model):
    hashPrecedent = models.CharField(max_length=100)
    actuel = models.CharField(max_length=100)
