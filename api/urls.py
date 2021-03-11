from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MovieAPI

router = DefaultRouter()
router.register('',MovieAPI)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]