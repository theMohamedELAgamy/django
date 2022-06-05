from django.shortcuts import redirect, render, reverse
from django.shortcuts import render
from urllib3 import HTTPResponse
from actor.models import Actor
from movie.forms import MovieForm
from movie.models import Movie

def movie_home(request):
     movies = Movie.objects.all()
     
     return (render (request,'movie/home.html',context={'movies':movies}))
      
def movie_create(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, template_name='movie/movie_create.html', context={'form': form})

    elif request.method == 'POST':
          form = MovieForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect(reverse('movie:home'))

def movie_details(request,**args):
     movie=Movie.objects.get(pk=args['id'])
     actors=Actor.objects.filter(movie=movie)
     return (render (request,'movie/details.html',context={'movie':movie,'actors':actors}))

def movie_delete(request,**args):
     movie = Movie.objects.get(pk=args['id'])
     movie.delete()
     return redirect(reverse('movie:home'))


def movie_update(request,**args):
     movie = Movie.objects.get(pk=args['id'])
     if request.method == 'GET':
               form = MovieForm(instance=movie)
               return render(request, template_name='movie/movie_update.html', context={'form': form, 'movie': movie})

     elif request.method == 'POST':
          form = MovieForm(request.POST,instance=movie)
          if form.is_valid():
               form.save()
               return redirect(reverse('movie:home'))