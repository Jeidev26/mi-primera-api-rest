from rest_framework import viewsets, permissions
from .models import Indices
from .serializers import IndicesSerializer

class IndicesViewSet(viewsets.ModelViewSet):
    queryset = Indices.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IndicesSerializer