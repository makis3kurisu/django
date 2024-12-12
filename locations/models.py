from django.db import models
from django.contrib.auth.models import User

class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='points')
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='point_images/', null=True, blank=True)  # Поле для изображения
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.point.name}'
