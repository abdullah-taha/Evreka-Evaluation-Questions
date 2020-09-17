from django.db import models


# models for question1

max_plate_size = 20


class Vehicle(models.Model):
    plate = models.CharField(max_length=max_plate_size)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.datetime) + str(self.vehicle)


# models for question2


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()


class Operation(models.Model):
    name = models.CharField(max_length=256)


class Collection(models.Model):
    bin_id = models.ForeignKey(Bin, null=True, on_delete=models.SET_NULL)
    operation_id = models.ManyToManyField(Operation)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()
