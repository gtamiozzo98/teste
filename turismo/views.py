from rest_framework import viewsets
from turismo.models import Restaurante,Hotel,Atrativo,Evento
from turismo.serializer import RestauranteSerializer,HotelSerializer,AtrativoSerializer,EventoSerializer

class RestauranteViewSet(viewsets.ModelViewSet): # precisa passar o queryset e o serializer_class
    queryset = Restaurante.objects.all()     #criar filtros
    serializer_class = RestauranteSerializer #classe seriliadora responsavel pelo RestauranteViewSet

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class AtrativoViewSet(viewsets.ModelViewSet):
    queryset = Atrativo.objects.all()
    serializer_class = AtrativoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer