from django.shortcuts import render,HttpResponse
from .models import Post
 

# Create your views here.
def blog(request):
    latest_post=Post.objects.all().order_by("-date")[:3]
    return  render(request,"blog/index.html",{
        "posts": latest_post
    })

 
def post(request):
    all_posts=Post.objects.all().order_by("-date")
    return  render(request,"blog/all-posts.html",{
        "all_post":all_posts
    }) 


def post_details(request,slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request,"blog/post-detail.html",{
        "posts":identified_post,
        "post_tags":identified_post.tags.all()
    })

