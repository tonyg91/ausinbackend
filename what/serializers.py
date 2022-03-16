from dataclasses import field, fields
from django.db import models
from rest_framework import serializers
from .models import What, Past, Deals, Sites

class WhatSerializer(serializers.ModelSerializer):
    class Meta:
        model = What 
        fields = ['id', 'event', 'description', 'date', 'location']
        
class PastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Past
        fields = ['id', 'pastevent', 'pastdescription', 'pastdate', 'pastlocation']
        
class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ['id', 'place', 'deal', 'previousprice', 'duration']
        
class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ['id', 'place', 'history', 'whattosee']
    