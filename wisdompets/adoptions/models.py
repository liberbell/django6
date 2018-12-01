from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Femail')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    bread = models.CharField(max_length=30, blank=True)
    descrption = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_data = models.Data
