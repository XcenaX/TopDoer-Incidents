from django.urls import path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api.views.incident import IncidentCreateView, IncidentListView, IncidentStatusUpdateView
from api.views.main import to_docs


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="Документация API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [  
    path("", to_docs, name="root-to-docs"),

    path("incidents/", IncidentListView.as_view(), name="incident-list"),
    path("incidents/create/", IncidentCreateView.as_view(), name="incident-create"),
    path("incidents/<uuid:incident_id>/status/", IncidentStatusUpdateView.as_view(), name="incident-status-update"),
    
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]