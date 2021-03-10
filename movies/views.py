from django.shortcuts import render, redirect,get_object_or_404
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index_func(request):
    welcome_message = "Welcome to IMDB!!!"
    context = {
        'welcome_message':welcome_message,
    }
    return render(request,'movies/home.html',context)

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/movies_list.html',context)


def movie_detail(request,id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie' : movie
    }
    return render(request,'movies/movie_detail.html',context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request,'movies/movie_form.html',{'form':form})


def movie_delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movie_list')

def movie_update(request,id):
    context = {}
    movie = get_object_or_404(Movie,id=id)
    form = MovieForm(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_detail',id=movie.id)
    context["form"] = form
    return render(request, "movies/movie_form.html", context)