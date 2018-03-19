from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^userName=(<str:userName>)&platform=(<str:platform>)$', views.graphs),
    url(r'^$', views.home),
    url('graphs.html', views.graphs),
]