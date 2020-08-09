
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', AccountViewSet, basename='user')
urlpatterns = router.urls

