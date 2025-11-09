from uuid import UUID
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.models.incident import Incident
from api.serializers.incident import IncidentCreateSerializer, IncidentListSerializer, IncidentStatusUpdateSerializer
from api.enums import IncidentSource, IncidentStatus


class IncidentCreateView(APIView):
    @swagger_auto_schema(
    operation_summary="Создать инцидент",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["text", "source"],
        properties={
            "text": openapi.Schema(type=openapi.TYPE_STRING, description="Описание"),
            "status": openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=[c[0] for c in IncidentStatus.choices],
                default=IncidentStatus.OPEN,
            ),
            "source": openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=[c[0] for c in IncidentSource.choices],
            ),
        },
    ),
    responses={201: openapi.Response("Созданный инцидент", IncidentCreateSerializer)},
)
    def post(self, request):
        serializer = IncidentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        incident = serializer.save()
        return Response(IncidentCreateSerializer(incident).data, status=status.HTTP_201_CREATED)


class IncidentListView(APIView):
    status_param = openapi.Parameter(
        name="status",
        in_=openapi.IN_QUERY,
        description="Фильтр по статусу. Если не указан вернёт все.",
        type=openapi.TYPE_STRING,
        required=False,
        enum=[c[0] for c in IncidentStatus.choices],
    )

    @swagger_auto_schema(
        operation_summary="Список инцидентов",
        manual_parameters=[status_param],
        responses={200: openapi.Response("Список", IncidentListSerializer(many=True))},
    )
    def get(self, request):
        qs = Incident.objects.all()
        status_filter = request.query_params.get("status")
        if status_filter:
            qs = qs.filter(status=status_filter)
        serializer = IncidentListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IncidentStatusUpdateView(APIView):
    @swagger_auto_schema(
        operation_summary="Обновить статус инцидента",
        operation_description=(
            "Обновляет только поле status по ID инцидента"            
        ),
        request_body=IncidentStatusUpdateSerializer,
        responses={
            200: openapi.Response("Обновлённый инцидент", IncidentListSerializer),
            400: "Некорректные данные",
            404: "Инцидент не найден",
        },
        examples={
            "application/json": {"status": "in_progress"}
        },
    )
    def patch(self, request, incident_id: str):
        print(incident_id)
        incident = get_object_or_404(Incident, pk=incident_id)
        serializer = IncidentStatusUpdateSerializer(incident, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(IncidentListSerializer(incident).data, status=status.HTTP_200_OK)
