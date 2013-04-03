from django.http import HttpResponse
from fbuser.models import Movie, User
def room(request):
    movie_list = Movie.objects.all();
    user_list = User.objects.all();
    output = ', '.join([p.title for p in movie_list])
    user_output = ','.join([p.name for p in user_list])
    output = '<p>Movie: ' + output + '</p><p>User: ' + user_output + '</p>'
    return HttpResponse(output)
