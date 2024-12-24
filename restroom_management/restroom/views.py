from django.shortcuts import render
from .models import RestroomStatus
from django.utils import timezone

def home(request):
    """
    View function for the home page of the site, showing the status of all restrooms.
    Each restroom's cleanliness is determined based on set thresholds for temperature,
    humidity, odour level, and toiletries stock.
    """
    statuses = RestroomStatus.objects.all()
    alerts = []  # List to store alert messages for dirty restrooms

    for status in statuses:
        # Check conditions to determine if the restroom is clean or dirty
        if status.temperature < 18 or status.temperature > 25 or \
           status.humidity < 30 or status.humidity > 60 or \
           status.odour_level > 5 or \
           not status.toiletries_stock:
            status.is_clean = False
            alerts.append(f"{status.restroom.name} restroom is dirty and needs immediate cleaning.")
        else:
            status.is_clean = True

        # Save the updated cleanliness status in the database
        status.save()

    # Render the HTML template, passing in data and alerts to be displayed
    return render(request, 'restroom/home.html', {'statuses': statuses, 'alerts': alerts})# from django.shortcuts import render
