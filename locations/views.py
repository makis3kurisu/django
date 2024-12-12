from rest_framework import viewsets, permissions
from .models import Point, Comment
from .serializers import PointSerializer, CommentSerializer
from django.shortcuts import render
class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all().order_by('-created_at')
    serializer_class = PointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def map_view(request):
    return render(request, 'locations/map.html')
