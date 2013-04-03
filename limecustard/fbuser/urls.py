from django.conf.urls import patterns, url

from fbuser import views

urlpatterns = patterns('',
    url(r'^$', views.room, name='room')
)
