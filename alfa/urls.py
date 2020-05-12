from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from alfa import views
from django.conf import settings 
from django.contrib.staticfiles.views import serve 
app_name="alfa"
urlpatterns = [
    url(r'^$', views.homepage,name='homepage'),
    url(r'update/',views.myupdate,name='myupdate'),
    url(r'list/',views.mylist,name="mylist"),
    url(r'watch/',views.watch,name='watch'),
]

if settings.DEBUG: 
    urlpatterns += [ url(r'^static/(?P<path>.*)$', serve), ]
