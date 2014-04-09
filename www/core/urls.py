from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^flare\.json', views.flare, name='flare'),
  url(r'^$', views.index, name='index'),
)
