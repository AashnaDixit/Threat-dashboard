from datetime import timedelta, date
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DailyThreatCount 
from .models import MonthlyLeakCount

class WeeklyActiveThreatsView(APIView):
    def get(self, request):
        # Calculate start and end of the current week
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        
        # Get the daily counts for the current week
        data = {}
        for i in range(7):
            day = start_of_week + timedelta(days=i)
            daily_threat = DailyThreatCount.objects.filter(date=day).first()  # Fetch from the DailyThreatCount model
            data[day.strftime('%Y-%m-%d')] = daily_threat.count if daily_threat else 0  # Use the count field

        return Response(data)
    
class MonthlyLeaksView(APIView):
    def get(self, request):
        # Get the current year (or any specific year passed as a query parameter)
        current_year = date.today().year
        
        # Fetch the monthly leak counts for the given year
        leaks = MonthlyLeakCount.objects.filter(year=current_year).order_by('month')
        
        # Prepare the data for the line graph (months and counts)
        months = []
        counts = []
        for leak in leaks:
            months.append(f"{leak.year}-{leak.month:02d}")  # Format month as YYYY-MM
            counts.append(leak.count)
        
        # If there are months missing in the data (for months with no leaks)
        for i in range(1, 13):
            if f"{current_year}-{i:02d}" not in months:
                months.append(f"{current_year}-{i:02d}")
                counts.append(0)

        # Return the data as a response
        return Response({"months": months, "counts": counts})    
