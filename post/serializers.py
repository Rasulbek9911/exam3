from rest_framework import serializers
from .models import Tag, Post, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if self.context['request'].user in data['chat'].members.all():
            return data
        raise serializers.ValidationError("")

    class Meta:
        model = Comment
        fields = '__all__'
