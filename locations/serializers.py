from rest_framework import serializers
from .models import Point, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

class PointSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(required=False)  # Поле изображения

    class Meta:
        model = Point
        fields = ['id', 'user', 'name', 'description', 'latitude', 'longitude', 'image', 'created_at']
