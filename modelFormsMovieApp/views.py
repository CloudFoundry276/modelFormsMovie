from django.shortcuts import render
from modelFormsMovieApp.forms import MovieForm
from modelFormsMovieApp.models import Movie


# Create your views here.
def index(request):
    return render(request, "modelFormsMovieApp/index.html")


def listMovies(request):
    movies_list = Movie.objects.all()
    return render(request, "modelFormsMovieApp/movies_list.html", {"movies": movies_list})


def addMovie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, "modelFormsMovieApp/movie_add.html", {"form": form})
