from django.db import models
from datetime import date

class Threat(models.Model):
    CATEGORY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    date_detected = models.DateField(default=date.today)  # Date when the threat was detected
    active = models.BooleanField(default=True)            # If the threat is currently active
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # Threat category

    def __str__(self):
        return f"{self.category} threat on {self.date_detected}"

class DailyThreatCount(models.Model):
    date = models.DateField(default=date.today)  # The date for which we store the count
    count = models.IntegerField(default=0)      # The number of active threats on that day

    def __str__(self):
        return f"Threat count for {self.date}: {self.count}"
    
from django.db import models

class MonthlyLeakCount(models.Model):
    year = models.IntegerField()  # Year when leaks occurred
    month = models.IntegerField()  # Month when leaks occurred
    count = models.IntegerField()  # Number of leaks in that month

    def __str__(self):
        return f"{self.month}/{self.year} - {self.count} leaks"

    class Meta:
        unique_together = ('year', 'month')  # Ensures unique combination of month and year
