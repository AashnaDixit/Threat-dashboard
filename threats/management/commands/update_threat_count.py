from django.core.management.base import BaseCommand
from datetime import date, timedelta
from threats.models import Threat, DailyThreatCount

class Command(BaseCommand):
    help = 'Updates the daily count of active threats'

    def handle(self, *args, **kwargs):
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())  # Get Monday of the current week
        end_of_week = start_of_week + timedelta(days=6)  # Get Sunday of the current week

        for i in range(7):
            day = start_of_week + timedelta(days=i)

            # Count active threats for that day
            active_threats_count = Threat.objects.filter(active=True, date_detected=day).count()

            # Check if there's already an entry for this day and update or create
            daily_threat, created = DailyThreatCount.objects.get_or_create(date=day)
            daily_threat.count = active_threats_count
            daily_threat.save()

            # Log output
            self.stdout.write(self.style.SUCCESS(f"Updated count for {day}: {active_threats_count}"))
