from rest_framework import serializers
from clients.models import Client

#serializer para listar, crear y detallar clientes
class ClientSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Client."""
    class Meta:
        model = Client
        fields = '__all__'
