from django.db.models import query
from django.shortcuts import render
from core.models import Currency, Category, Transaction
from rest_framework import generics
from rest_framework import viewsets
from core.serializers import CurrencySerializer, CategorySerializer, WriteTransactionSerializer, ReadTransactionSerializer
# Create your views here.

class CurrenceListApiView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related('currency','category')
    serializer_class = ReadTransactionSerializer

    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return ReadTransactionSerializer
        return WriteTransactionSerializer

