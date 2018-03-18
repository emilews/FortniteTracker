from django.shortcuts import render
from .forms import SearchForm


def home(request):
    return render(request, 'track/index.html')


def graphs(request):

    username = request.GET['user']
    return render(request,'track/graphs.html', {'userName' : username})


