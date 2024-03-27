# views.py
from rest_framework import viewsets
from clients.models import Client
from clients.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Client."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
