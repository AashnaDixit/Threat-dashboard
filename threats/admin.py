from django.contrib import admin
from .models import Threat, DailyThreatCount, MonthlyLeakCount

# Registering the models for the admin interface
admin.site.register(Threat)
admin.site.register(DailyThreatCount)

@admin.register(MonthlyLeakCount)
class MonthlyLeakCountAdmin(admin.ModelAdmin):
    list_display = ('get_month_name', 'year', 'count')  # Use get_month_name to show the month name
    search_fields = ('month', 'year')

    def get_month_name(self, obj):
        # Return the full name of the month
        from calendar import month_name
        return month_name[obj.month]  # Use the month number to get the full month name

    get_month_name.admin_order_field = 'month'  # Allow sorting by month
    get_month_name.short_description = 'Month'  # Display label in the admin