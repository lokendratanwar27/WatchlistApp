from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


@api_view(['GET','POST'])
def movie_list(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialzer = MovieSerializer(movies,many =True)
        return Response(serialzer.data) 
        
       
    if request.method == 'POST':
        serialzer = MovieSerializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)
        
        
@api_view(['GET', 'PUT','DELETE']) 
def movie_details(request,pk): 
    
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error":"Movie Does not exist"},status='HTTP_404_NOT_FOUND')

        serialzer = MovieSerializer(movie)
        return Response(serialzer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serialzer = MovieSerializer(movie, data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
        
        
