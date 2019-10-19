from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, SavePost
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import login as do_login

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    saves="no"
    post = get_object_or_404(Post, pk=pk)
    save_posts = SavePost.objects.all()
    for save in save_posts:
        if save.save_user == request.user.username:
            if save.save_post==post:
                saves="yes";
                break;
    return render(request, 'blog/post_detail.html', {'post': post, 'saves' : saves, 'no':"no"})

@login_required
def post_new(request):
    saves = SavePost.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    saves = SavePost.objects.all()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts=[]
    post_list = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    for post in post_list:
        if post.author== request.user.username:
            posts.append(post)
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    saves = SavePost.objects.all()
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post-detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post-list')

@login_required
def post_save(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.save = SavePost.objects.create(save_post=post, save_user=request.user.username)
    saves = SavePost.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'saves':saves})

@login_required
def post_save_list(request):
    saves=[]
    save_posts = SavePost.objects.all()
    for save in save_posts:
        if save.save_user== request.user.username:
            saves.append(save)
    return render(request, 'blog/post_save_list.html', {'posts': saves})

@login_required
def save_remove(request, pk):
    save_post = get_object_or_404(SavePost, pk=pk)
    save_post.delete()
    return redirect('blog:post-save-list')

@login_required
def add_comment_to_post(request, pk):
    saves = SavePost.objects.all()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.approve()
            comment.save()
            return redirect('blog:post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    saves = SavePost.objects.all()
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post-detail', pk=comment.post.pk)

def register(request):
    form = UserCreationForm()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "registration/register.html", {'form': form})

@login_required
def user(request):
    posts = Post.objects.filter(author=request.user).order_by('-published_date')
    return render(request, "user/user.html", {'posts': posts})

@login_required
def user_config(request):
    return render(request, 'user/user_config.html')

@login_required    
def user_eliminate(request):
    me = get_object_or_404(User, username=request.user.username)
    posts = Post.objects.all()
    comments = Comment.objects.all()
    for post in posts:
        if post.author == request.user.username:
            post.delete()
    for com in comments:
        if com.author == request.user.username:
            com.delete()
    me.delete()
    return redirect('/')
