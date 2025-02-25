from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogComment


# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    comments = BlogComment.objects.all()
    return render(request, 'index.html', context={'posts': posts})
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=pk)
    comment = BlogComment.objects.filter(post=post)
    return render(request, 'post_details.html', context={'post': post, 'comments': comment})



