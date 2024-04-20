from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    ID=models.IntegerField(_("ID"),max_length=30)
    Status=models.CharField(_("Status"),max_length=10,choices=Status_type)

    def __str__(self):
        return self.ID


class Station(models.Model):
    ID=models.IntegerField(_("ID"),max_length=30)
    Name=models.CharField(_("Name"),max_length=20)
    FamousPlaces=models.CharField(_("FamousPlaces"),max_length=50)
    def __str__(self):
        return self.Name    

class Ticket(models.Model):
    StationID=models.ForeignKey("station",verbose_name=_("StationID"),related_name="ticket_station", on_delete=models.SET_NULL,null=True)
    Cost=models.FloatField(_("Cost"),)
    Time=models.FloatField(_("Time"),)    
    def __str__(self):
        return self.StationID