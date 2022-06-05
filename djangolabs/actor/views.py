from django.shortcuts import redirect, render, reverse
from actor.forms import ActorForm
from actor.models import Actor
from movie.models import Movie




def actor_home(request):
     actors = Actor.objects.all()
     return (render (request,'actor/home.html',context={'actors':actors}))

def actor_details(request,**args):
     actor=Actor.objects.get(pk=args['id'])
     movies=Movie.objects.filter(actors=actor)
     return (render (request,'actor/details.html',context={'actor':actor,'movies':movies}))

def actor_delete(request,**args):
     actor = Actor.objects.get(pk=args['id'])
     actor.delete()
     return redirect(reverse('actor:home'))


def actor_create(request):
    if request.method == 'GET':
        form = ActorForm()
        return render(request, template_name='actor/create_actor.html', context={'form': form})

    elif request.method == 'POST':
          form = ActorForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect(reverse('actor:home'))
 

def actor_update(request,**args):
     actor = Actor.objects.get(pk=args['id'])
     if request.method == 'GET':
               form = ActorForm(instance=actor)
               return render(request, template_name='actor/actor_update.html', context={'form': form, 'actor': actor})

     elif request.method == 'POST':
          form = ActorForm(request.POST,request.FILES,instance=actor)
          if form.is_valid():
               form.save()
               return redirect(reverse('actor:home'))


