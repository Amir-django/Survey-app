from django.db import models

# Create your models here.
class surveyData(models.Model):
    first = models.CharField(max_length=100)
    secound = models.CharField(max_length=100, default=None)
    third = models.CharField(max_length=100, default=None)
    fourth = models.CharField(max_length=100, default=None)
    fifth = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.first