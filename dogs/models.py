from django.db import models
from django.db.models import aggregates
from django.db.models.fields import CharField

class Owners(models.Model):
    name    = models.CharField(max_length=45)
    email   = models.CharField(max_length=300)
    age     = models.IntegerField()

    class Meta:
        db_table = "owners"

class Dogs(models.Model):
    owner    = models.ForeignKey("Owners",on_delete=models.CASCADE)
    name     = models.CharField(max_length=45)
    age      = models.IntegerField()

    class Meta:
        db_table = "dogs"


