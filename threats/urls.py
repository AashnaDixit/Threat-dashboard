from django.urls import path
from .views import WeeklyActiveThreatsView
from .views import MonthlyLeaksView


urlpatterns = [
    path('api/active-threats-weekly/', WeeklyActiveThreatsView.as_view(), name='weekly-active-threats'),
    path('api/monthly-leaks-line-graph/', MonthlyLeaksView.as_view(), name='monthly-leaks-line-graph'),
]
