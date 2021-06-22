from django.db import models

# Create your models here.
class Match(models.Model):
    mname=models.CharField(max_length=200)
    teams=models.CharField(max_length=200)
    team2=models.CharField(max_length=200)
    mcout=models.IntegerField()
    venue=models.CharField(max_length=250)
    time=models.CharField(max_length=200)
    date=models.DateField()
    icon1=models.ImageField()
    icon2=models.ImageField()
    def __str__(self):
        return self.mname