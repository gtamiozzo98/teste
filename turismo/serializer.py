from rest_framework import serializers
from turismo.models import Restaurante,Hotel,Atrativo,Evento

class RestauranteSerializer(serializers.ModelSerializer): # transforma o model em json
    class Meta:
        model = Restaurante
        fields = '__all__' #informações que serão disponibilizadas para api

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class AtrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrativo
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'