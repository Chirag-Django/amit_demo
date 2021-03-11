from django.shortcuts import render
from .serializers import MovieSerializer
from movies.models import Movie
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
# Create your views here.

class MovieAPI(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

