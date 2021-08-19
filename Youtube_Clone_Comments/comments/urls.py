from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.Comments.as_view()),  # comments on video
    path('comment/<int:id>', views.CommentDetail.as_view()),
]
