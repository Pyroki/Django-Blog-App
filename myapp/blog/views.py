from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from blog.models import Post,Category
from .forms import PostForm, RegisterForm, LoginForm,ForgotPasswordForm
from django.contrib.auth import authenticate,logout as auth_logout
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator

# Blog index view
def index(request):
    blog_title = "Latest Posts"
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_obj})

# Post detail view
def detail(request, slug):
    post = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    return render(request, 'detail.html', {"post": post, "related_posts": related_posts})

# Contact view
def contact(request):
    return render(request, "contact.html")

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print('Register success') # Redirect to login page after successful registration
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

# User login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                print('Login success')
                return redirect('blog:dashboard')  # Redirect to the homepage after login
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def dashboard(request):
    b='My Posts'
    all_posts = Post.objects.filter(user=request.user)

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'dashboard.html',{'b':b,'page_obj':page_obj})

def logout(request):
    auth_logout(request)
    return redirect('blog:login')

def forgot_password(request):
    if request.method =='POST':

        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user= User.objects.get(email=email)

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            domain = current_site.domain
            subject = 'Reset password Requested'
            message = render_to_string('blog/reset_passsword.html',{'domain':domain})


         
    return render(request,'forgot_password.html')


def new_post(request):

    form = PostForm()
    categories = Category.objects.all()


     
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:dashboard")

    return render (request,'new_post.html',{'categories':categories,"form":form} )

def edit_post(request,post_id):
    form=PostForm()
    categories = Category.objects.all()
    post = get_object_or_404(Post,slug=post_id)

    if request.method =='POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:dashboard')

    return render(request,'edit_post.html',{'categories':categories,'post':post,'form':form})

def delete_post(request,post_id):
    post = get_object_or_404(Post,slug=post_id)
    post.delete()
    return redirect('blog:dashboard')