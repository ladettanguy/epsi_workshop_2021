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
    parti = models.CharField(max_length=20)
    description = models.CharField(max_length=200)


class Block(models.Model):
    id_block = models.IntegerField(default=0)
    hashPrecedent = models.CharField(max_length=100)
    actuel = models.CharField(max_length=100)
    hashSuivant = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
