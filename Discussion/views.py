from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Discussion, Comment
from .serializators import DiscussionSerializer, CommentSerializer

class CRUD_Discussion(ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class CRUD_Comment(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

        
