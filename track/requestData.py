from django.shortcuts import render
import requests, json

def graphs(request):

    return render(request, 'track/graphs.html')