from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flight, Booking
from .forms import BookingForm
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_app/flight_list.html', {'flights': flights})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('flight_list')  # change this to your actual home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flight_list')  # or your homepage
    else:
        form = UserCreationForm()
    return render(request, 'flight_app/signup.html', {'form': form})

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.flight = flight
            booking.save()
            # After booking, redirect to payment page
            return redirect('payment_page', booking_id=booking.id)
    else:
        form = BookingForm(initial={'flight': flight})

    return render(request, 'flight_app/book_flight.html', {'form': form, 'flight': flight})

@login_required
def booking_success(request):
    return render(request, 'flight_app/booking_success.html')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'flight_app/my_bookings.html', {'bookings': bookings})

@login_required
def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        # Here you would process payment logic
        # For simplicity, just redirect to success page after 'payment'
        return redirect('booking_success')

    return render(request, 'flight_app/payment_page.html', {'booking': booking})
