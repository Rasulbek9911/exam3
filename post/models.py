from django.db import models
from author.models import Author


# Create your models here.
class Tag(models.Model):
    title = models.CharField()


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    subcontent = models.TextField()
    image = models.FileField()

    tag = models.ManyToManyField(Tag)
    view_count = models.PositiveIntegerField()
    read = models.PositiveIntegerField()

    is_popular = models.BooleanField(default=False)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_at = models.DateField()
    update_at = models.DateField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

    create_at = models.DateField()
    update_at = models.DateField()
