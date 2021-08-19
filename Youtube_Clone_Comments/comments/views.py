from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# All comments
class Comments(APIView):
    def get(self, request, video_id):
        comments = Comment.objects.filter(video_id=video_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, video_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Specific video comments


class CommentDetail(APIView):
    def get(self, request, id):
        comment = Comment.objects.filter(id=id)
        if comment:
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        comment = Comment.objects.get(id=id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentLike(APIView):
    def get_object(self, pk, video_id):
        try:
            return Comment.objects.get(pk=pk, video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk, video_id):
        comment = self.get_object(pk, video_id=video_id)
        data = {"likes": comment.likes + int(1)}
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
