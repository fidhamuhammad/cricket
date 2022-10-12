from django.shortcuts import render

# Create your views here.
def player_home(request):
    return render(request,'player_template/home.html')

def player_domestic(request):
    return render(request,'player_template/domestic.html')   

def player_videos(request):
    return render(request,'player_template/videos.html') 

def player_play(request):
    return render(request,'player_template/play.html')     

  



