from django.db.models import query
from django.shortcuts import render
from core.models import Currency,Category
from rest_framework import generics
from rest_framework import viewsets
from core.serializers import CurrencySerializer,CategorySerializer
# Create your views here.

class CurrenceListApiView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
