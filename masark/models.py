from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    id=models.IntegerField(_("ID"))
    status=models.CharField(_("Status"),max_length=10,choices=Status_type)

    def __str__(self):
        return self.id


class Station(models.Model):
    id = models.IntegerField(_("Id"))  # Renamed to lowercase 'id'
    Name = models.CharField(_("Name"), max_length=20)
    FamousPlaces = models.CharField(_("FamousPlaces"), max_length=50)
    
    def __str__(self):
        return self.Name
   

class Ticket(models.Model):
    StationID = models.ForeignKey("Station", verbose_name=_("StationID"), related_name="ticket_station", on_delete=models.SET_NULL, null=True)
    Cost = models.FloatField(_("Cost"))
    Time = models.FloatField(_("Time"))

    def __str__(self):
        return str(self.StationID)  # Ensure to return a string representation
