from django.shortcuts import render
from rest_framework import generics
from .models import Tag, Post, Comment
from .serializers import TagSerializer, PostSerializer, CommentSerializer
from helpers.pagination import CustomPagination


# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    pagination_class = CustomPagination()
    serializer_class = PostSerializer


class PostListRetrieve(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListIsPopular(generics.ListAPIView):
    queryset = Post.objects.filter(is_popular=True)
    pagination_class = CustomPagination()
    serializer_class = PostSerializer


class PostListForYou(generics.ListAPIView):
    queryset = Post.objects.all()
    pagination_class = CustomPagination()
    serializer_class = PostSerializer


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer()


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer()

    def get_queryset(self):
        queryset = self.queryset
        post_id = self.kwargs.get('post_id')
        queryset = queryset.filter(post=post_id)
        return queryset
