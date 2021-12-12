from django.contrib import admin
from core.models import Currency
from core.models import Category
from core.models import Transaction

# Register your models here.
admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Transaction)
