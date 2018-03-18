from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.home),
        url(r'^graphs', views.graphs),
    ]