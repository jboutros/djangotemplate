from django.conf.urls import patterns, url
from firstapp.views import app_home

urlpatterns = patterns('',
    url(r'^$', app_home, name='app_home'),
)