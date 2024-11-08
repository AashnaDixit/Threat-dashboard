from rest_framework import serializers
from .models import Threat

class ThreatSerializer(serializers.ModelSerializer):
    date_detected = serializers.DateField(format="%Y-%m-%d")  # Convert date to string format

    class Meta:
        model = Threat
        fields = ['date_detected', 'category', 'active']
