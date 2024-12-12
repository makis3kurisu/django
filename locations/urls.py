from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PointViewSet, CommentViewSet

# Маршруты для API
router = DefaultRouter()
router.register(r'points', PointViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Маршрут для карты
    path('map/', views.map_view, name='map'),

    # Маршруты для API
    path('api/', include(router.urls)),
    path('media/', include(router.urls))
]
