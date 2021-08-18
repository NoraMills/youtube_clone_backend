from Youtube_Clone_Comments.comments.serializers import CommentSerializer
from Youtube_Clone_Comments.comments.models import Comment
from django.shortcuts import render
from rest_framework.views import APIView
# serializers
from rest_framework.response import Response
from rest_framework import serializers, status
# from django.http import Http404 ?

# Create your views here.


class Comments(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
