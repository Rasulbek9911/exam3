from django.urls import path
from .views import *

urlpatterns = [
    path('PostList/', PostList.as_view()),
    path('PostListRetrieve/<int:pk>', PostListRetrieve.as_view()),
    path('PostListIsPopular/', PostListIsPopular.as_view()),
    path('PostListForYou/', PostListForYou.as_view()),
    path('CommentCreate/', CommentCreate.as_view()),
    path('CommentList/<post_id>', CommentList.as_view()),
]
