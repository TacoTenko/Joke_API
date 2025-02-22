from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Joke
from .serializers import JokeSerializer
from .services import get_all_jokes, get_joke_by_id, create_joke, update_joke, delete_joke

@api_view(['GET', 'POST'])
def joke_list(request):
    if request.method == 'GET':
        category = request.query_params.get('category', None)  # Get category from query params
        jokes = get_all_jokes(category)  # Fetch jokes with optional filtering
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def joke_detail(request, joke_id):
    joke = get_joke_by_id(joke_id)
    if not joke:
        return Response({"error": "Joke not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JokeSerializer(joke)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JokeSerializer(joke, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        delete_joke(joke)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def top_rated_jokes(request):
    jokes = Joke.objects.exclude(rating__isnull=True).order_by('-rating')[:10]
    serializer = JokeSerializer(jokes, many=True)
    return Response(serializer.data)
