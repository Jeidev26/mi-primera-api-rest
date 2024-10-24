from rest_framework import routers
from .viewsets import IndicesViewSet

router = routers.DefaultRouter()

router.register('api/indices', IndicesViewSet, 'ruta_indices')

urlpatterns = router.urls