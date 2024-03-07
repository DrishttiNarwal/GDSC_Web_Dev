from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("our_team.html", views.our_team, name="our_team"),
    path("about.html", views.about, name="about"),
    path('index.html', views.index, name='index'),
    path("tracks.html", views.tracks, name="tracks"),
    path("events.html", views.events, name="events"),
    path("contact.html", views.contact, name="contact"),
    path("gallery.html", views.gallery, name="gallery")
]
