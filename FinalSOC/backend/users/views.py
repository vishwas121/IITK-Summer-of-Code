from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CirculationHistorySerializer
from .models import Circulation
from rest_framework.response import Response

# Create your views here.

class CirculationView(viewsets.ModelViewSet):
    serializer_class = CirculationHistorySerializer

    def get_queryset(self):
        return Circulation.objects.all()

    def list(self,request):
        queryset = self.get_queryset()
        serializer = CirculationHistorySerializer(queryset,many=True)

        return Response(serializer.data)
    def create(self,request):
        data = request.data
        serializer = CirculationHistorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors ,status =400)
