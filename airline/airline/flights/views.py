from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight)
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = get_object_or_404(Flight, pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        passenger.flights.add(flight)
        return redirect("flight", flight_id=flight_id)
