from django.http import HttpResponse
from django.template import Context, loader
from fbuser.models import Movie, User
from django.shortcuts import render

def room(request):
    movie_list = Movie.objects.all();
    user_list = User.objects.all();

    #template = loader.get_template('room/index.html')
    context = Context({ 'movie_list': movie_list })
    return render(request, 'room/index.html', context)
