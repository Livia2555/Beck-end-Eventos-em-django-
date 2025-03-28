from .models import Evento
from rest_framework import serializers

class EventoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'