from django.shortcuts import render
from .models import Evento
from rest_framework.response import Response
from .serializers import EventoSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

# Create your views here.

@api_view(['GET'])
def read_eventos(request):
    
    eventos = Evento.objects.all()

    categoria = request.query_params.get('Categoria')
    data = request.query_params.get('Data')
    quantidade = request.query_params.get('quantidade')
    ordem = request.query_params.get('ordem')

    if categoria:
        eventos = eventos.filter(Categoria__icontains= categoria)

    if data:
        eventos = eventos.filter(DataHora__date= data)

    if quantidade:
        try:
            quantidade = int(quantidade)
            eventos = eventos[:quantidade]  # Limitar os eventos pelo valor de quantidade
        except ValueError:
            return Response({'erro': 'Quantidade deve ser um número inteiro'}, status=status.HTTP_400_BAD_REQUEST)


    if ordem =='data':
        eventos = eventos.order_by('DataHora')
    
    serializer = EventoSerializers(eventos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_evento(request,pk):
    try:
        evento= Evento.objects.get(pk=pk)

    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer =EventoSerializers(evento, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_evento(request,pk):
    try:
        evento= Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response({"mensagem": "evento apagado com sucesso"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def proximo_eventos(request):
    hoje = datetime.now().date()
    semana = hoje + timedelta(days=7)

    eventos = Evento.objects.filter(DataHora__date__range=[hoje, semana])
    
    serializer = EventoSerializers(eventos, many=True)
    return Response(serializer.data)



@api_view (['GET'])
def read_evento(request, pk):
    try:
        evento= Evento.objects.get(pk=pk)
    
    except Evento.DoesNotExist:
        return Response({'Erro': 'Este evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializers(evento)
    return Response(serializer.data)


















    

    




