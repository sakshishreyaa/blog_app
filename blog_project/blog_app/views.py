from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.

def index(req):
    return HttpResponse(("home"))

@login_required()
def create_post(req):
    if req.method=='GET':
        return render(req,'create_post.html')
    elif req.method=='POST':
        new_post=Post.objects.create(heading=req.POST['Heading'],content=req.POST['Content'],author=req.user)
        new_post.save()
        return HttpResponse('post creeated')
    else:
        return HttpResponse('error')
    
@login_required()
def view_post(req):
    all_posts=Post.objects.all().filter(author=req.user)
    context={
        'posts':all_posts
    }
    return render(req, 'view_post.html',context)
