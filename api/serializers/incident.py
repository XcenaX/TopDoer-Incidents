# serializers.py
from rest_framework import serializers
from api.models.incident import Incident


class IncidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["id", "text", "status", "source", "created_at"]
        read_only_fields = ["id", "created_at"]

class IncidentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["id", "text", "status", "source", "created_at"]

class IncidentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["status"]
