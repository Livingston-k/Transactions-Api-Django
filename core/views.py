from core.models import Currency, Category, Transaction
from rest_framework import generics
from rest_framework import viewsets
from core.serializers import CurrencySerializer, CategorySerializer, WriteTransactionSerializer, ReadTransactionSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CurrenceListApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AllTransactionModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.select_related(
        'currency', 'category', 'user')
    serializer_class = ReadTransactionSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserTransactionModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReadTransactionSerializer

    def get_queryset(self):
        return Transaction.objects.select_related('currency', 'category', 'user').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
