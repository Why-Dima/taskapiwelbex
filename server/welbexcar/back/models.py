from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=64)
    state_name = models.CharField(max_length=64)
    zip = models.PositiveIntegerField()
    lat = models.FloatField()
    lng = models.FloatField()


class Cargo(models.Model):
    loc_pick_up = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='loc_pick_up')
    loc_delivery = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='loc_delivery')
    weight = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=256)
    zip = models.PositiveIntegerField()


class Car(models.Model):
    number = models.CharField(max_length=5)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    carrying_capacity = models.PositiveIntegerField()
    zip = models.PositiveIntegerField()

