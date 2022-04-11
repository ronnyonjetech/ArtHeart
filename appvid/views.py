from django.shortcuts import render
from .models import Video
# Create your views here.


def appvidfunction(request):
    vid = Video.objects.all()
    return render(request, 'video.html', {'vid': vid})
