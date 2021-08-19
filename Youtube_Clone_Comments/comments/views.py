from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get_object(self, video_id):
        try:
            return Comment.objects.filter(video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, video_id):
        comment = self.get_object(video_id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def put(self, request, video_id):
        comment = self.get_object(video_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, video_id):
        comment = self.get_object(video_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLike(APIView):
    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        comment = self.get_object(id)
        data = {"likes": comment.likes + int(1)}
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDislike(APIView):
    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, id):
        comment = self.get_object(id=id)
        data = {"dislikes": comment.dislikes + int(1)}
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyList(APIView):
    def get(self, request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyDetail(APIView):
    def get_object(self, comment):
        try:
            return Reply.objects.filter(comment=comment)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment):
        reply = self.get_object(comment)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def put(self, request, comment):
        reply = self.get_object(comment)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment):
        reply = self.get_object(comment)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
