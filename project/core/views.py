from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse


# Create your views here.
def frontPage(request):
    posts= Post.objects.filter(status=Post.ACTIVE )
    context = {'posts': posts}
    return render(request, 'core/frontpage.html', context)

def About(request):
    return render(request, 'core/about.html')    

def robot_txt(request):
    text = [
        "User-Agent: *","Disallow: /admin/",
    ]    
    return HttpResponse("\n".join(text), content_type="text/plain")