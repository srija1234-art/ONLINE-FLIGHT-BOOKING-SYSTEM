from django.db import models
from django.conf import settings

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, null=True)
    origin = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.flight_number}: {self.origin} -> {self.destination}"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    passengers = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)  # new field

    def __str__(self):
        return f"Booking by {self.user} for {self.passengers} passengers"
