from nturl2path import url2pathname
from django.urls import path
from .import views

urlpatterns=[
    path('home',views.player_home),
    path('domestic',views.player_domestic),
    path('videos',views.player_videos),
    path('play',views.player_play)
   
]