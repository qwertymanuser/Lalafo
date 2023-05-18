from rest_framework import serializers
from apps.posts.models import Post, FavoritePost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'price', 'image', 'is_active', 'created', 'user', 'category')

class FavoritePostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ('if', 'user', 'post')

class PostDetailSerializer(serializers.ModelSerializer):
    post_favorite_users = FavoritePostSerializer(many=True, read_only=True)
    count_favorites = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'price', 'image', 'is_active', 'created', 'user', 'category', 'post_favorite_users', 'count_favorites')

    def get_count_favorites(self, obj):
        return obj.post_favorite_users.all().count()