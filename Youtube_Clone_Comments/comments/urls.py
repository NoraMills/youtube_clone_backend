from django.urls import path
from . import views
from .models import Comment

urlpatterns = [
    path('comments/', views.Comments.as_view()),
]
