from django.db import models
from django.utils import timezone

Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    ID=models.IntegerField(max_length=30)
    status=models.CharField(max_length=10)


class Station(models.Model):
    ID=models.IntegerField(max_length=30)
    Name=models.CharField(max_length=20)
    FamousPlaces=models.CharField(max_length=50)
    Tickets=models.ForeignKey("Ticket",related_name=("station_ticket"), on_delete=models.CASCADE)

class Ticket(models.Model):
    ID=models.IntegerField(max_length=30)
    StationID=models.IntegerField(max_length=30)
    Cost=models.FloatField()
    Time=models.FloatField()    