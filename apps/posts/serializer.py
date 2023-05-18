from rest_framework import serializers
from apps.posts.models import Post, FavoritePost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'price', 'image', 'is_active', 'created', 'user', 'category')

class FavoritePostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ('if', 'user', 'post')