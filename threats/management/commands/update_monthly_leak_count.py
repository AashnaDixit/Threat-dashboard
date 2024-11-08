from django.core.management.base import BaseCommand
from datetime import date, timedelta
from threats.models import Threat, MonthlyLeakCount
from django.db.models import Count
from django.db.models.functions import TruncMonth

class Command(BaseCommand):
    help = 'Updates the monthly count of active leaks'

    def handle(self, *args, **kwargs):
        today = date.today()
        start_of_month = today.replace(day=1)  # First day of the current month
        end_of_month = today.replace(day=28) + timedelta(days=4)  # Last day of the current month

        # Filter threats by active status and group by the month
        threats_by_month = Threat.objects.filter(active=True, date_detected__range=[start_of_month, end_of_month]) \
            .annotate(month=TruncMonth('date_detected')) \
            .values('month') \
            .annotate(count=Count('id')) \
            .order_by('month')

        for threat in threats_by_month:
            month = threat['month']
            count = threat['count']
            
            # Check if there's already an entry for this month
            monthly_leak, created = MonthlyLeakCount.objects.get_or_create(date=month)
            monthly_leak.count = count
            monthly_leak.save()

            self.stdout.write(self.style.SUCCESS(f"Updated count for {month}: {count}"))
