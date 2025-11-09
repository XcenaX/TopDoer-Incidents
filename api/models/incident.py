from django.db import models
from api.enums import IncidentSource, IncidentStatus
import uuid

class Incident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(verbose_name="Description")
    status = models.CharField(
        max_length=32,
        choices=IncidentStatus.choices,
        default=IncidentStatus.OPEN,
        db_index=True,
    )
    source = models.CharField(
        max_length=32,
        choices=IncidentSource.choices,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"#{self.pk} {self.status}"