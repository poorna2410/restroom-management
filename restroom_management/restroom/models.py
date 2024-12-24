from django.db import models
from django.utils import timezone
from datetime import timedelta

class Restroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class RestroomStatus(models.Model):
    restroom = models.ForeignKey(Restroom, on_delete=models.CASCADE)
    date = models.DateField()
    entries = models.IntegerField(default=0)
    exits = models.IntegerField(default=0)
    temperature = models.FloatField()
    humidity = models.FloatField()
    odour_level = models.IntegerField()
    toiletries_stock = models.BooleanField(default=True)
    is_clean = models.BooleanField(default=True)
    # New fields
    cleaned_date = models.DateField(null=True, blank=True)  # Date when last cleaned
    next_cleaning_date = models.DateField(null=True, blank=True)  # Date for the next cleaning

    def mark_as_cleaned(self):
        """Mark the restroom as cleaned and update the cleaning dates."""
        self.cleaned_date = timezone.now().date()  # Set cleaned_date to today
        self.next_cleaning_date = self.cleaned_date + timedelta(days=7)  # Set next_cleaning_date 7 days later
        self.is_clean = True  # Update the clean status
        self.save()
