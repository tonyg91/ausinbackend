from django.shortcuts import render
from .models import What, Past, Deals, Sites
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WhatSerializer, PastSerializer, DealsSerializer, SitesSerializer

# Create your views here.

class WhatViewSet(viewsets.ModelViewSet):
    queryset = What.objects.all()
    serializer_class = WhatSerializer
    permission_class = [permissions.AllowAny]
    
class PastViewSet(viewsets.ModelViewSet):
    queryset = Past.objects.all()
    serializer_class = PastSerializer
    permission_class = [permissions.AllowAny]
    
class DealsViewSet(viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer
    permission_class = [permissions.AllowAny]
    
class SitesViewSet(viewsets.ModelViewSet):
    queryset = Sites.objects.all()
    serializer_class = SitesSerializer
    permission_class = [permissions.AllowAny]