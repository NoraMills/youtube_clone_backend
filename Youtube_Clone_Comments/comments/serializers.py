from django.db import models
from rest_framework import serializers
from .models import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video_id', 'body', 'likes', 'dislikes']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['comment', 'body']
