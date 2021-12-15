from django.urls import path
from core import views as CoreViews
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', CoreViews.CategoryModelViewSet,
                basename='category')
router.register(r'transactions', CoreViews.TransactionModelViewSet,
                basename='transactions')

urlpatterns = [
    path('currencies/', CoreViews.CurrenceListApiView.as_view(), name='currencies'),
]+router.urls
