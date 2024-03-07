from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'gdsc/index.html')

# def index(request):
#    return render(request, 'index.html')


def tracks(request):
    return render(request, 'tracks.html')


def tracks_view(request):
    return render(request, 'tracks.html')


def index_view(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def about_view(request):
    return render(request, 'about.html')


def our_team(request):
    return render(request, 'our_team.html')


def our_team_view(request):
    return render(request, 'our_team.html')


def my_view(request):
    return render(request, 'image.html')


def events(request):
    return render(request, 'events.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def gallery_views(request):
    return render(request, 'gallery.html')
