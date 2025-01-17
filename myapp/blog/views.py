from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from blog.models import Post
from django.core.paginator import Paginator

# posts=[
#         {"id":1,'title':'Post 1','content':"content of post 1"},
#         {"id":2,'title':'Post 2','content':"content of post 2"},
#         {"id":3,'title':'Post 3','content':"content of post 3"},
#         {"id":4,'title':'Post 4','content':"content of post 4"}
#     ]

# Create your views here.
def index(request):
    blog_title="Latest Post"
    all_posts= Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    

     
    return render(request,'index.html',{'blog_title':blog_title,'page_obj':page_obj})

def detail(request, slug):
    # post=next((item for item in posts if item['id']==int(post_id)),None)
    post = Post.objects.get(slug=slug)
    related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    return render(request,'detail.html',{"post":post,"related_posts":related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:newurl')) 

def new_url(request):
    return HttpResponse('you are seeing the new URL')
