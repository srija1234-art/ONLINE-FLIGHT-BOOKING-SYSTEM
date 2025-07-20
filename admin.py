from django.contrib import admin
from .models import Flight, Booking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin', 'destination', 'departure_time', 'arrival_time')
    search_fields = ('flight_number', 'origin', 'destination')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'passengers')
    search_fields = ('user__username', 'flight__flight_number')
