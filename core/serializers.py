from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Category, Currency, Transaction


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'code']


class CategorySerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'user']


class WriteTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "amount",
            "user",
            "currency",
            "date",
            "description",
            "category"]


class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "user",
            "currency",
            "date",
            "description",
            "category",
            "user"
        ]
