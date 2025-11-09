from django.db import models

class IncidentStatus(models.TextChoices):
    OPEN = "open", "Open"
    IN_PROGRESS = "in_progress", "In Progress"
    RESOLVED = "resolved", "Resolved"
    CLOSED = "closed", "Closed"

class IncidentSource(models.TextChoices):
    OPERATOR = "operator", "Operator"
    MONITORING = "monitoring", "Monitoring"
    PARTNER = "partner", "Partner"