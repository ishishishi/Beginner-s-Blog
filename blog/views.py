from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.views.decorators.http import require_POST

def top(request):
    posts = Post.objects.all().order_by('-created_datetime')
    return render(request, 'blog/top.html', {'posts': posts})

def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    user_posts = Post.objects.filter(user=pk).order_by('-created_datetime')
    return render(request, 'blog/user_detail.html', {'user': user, 'user_posts': user_posts, 'post_detail': post_detail})

def post_detail(request, pk):
    post_detail = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post_detail': post_detail})

def sign_up(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                input_username = form.cleaned_data['username']
                input_password = form.cleaned_data['password1']
                new_user = authenticate(username=input_username, password=input_password)
                if new_user is not None:
                    login(request, new_user)
                    return redirect('blog:top')
        else:
            form = UserCreationForm()
        return render(request, 'blog/sign_up.html', {'form': form})

@login_required
def posts_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
        return redirect('blog:user_detail', pk=request.user.pk)
    else:
        form = PostForm()
    return render(request, 'blog/posts_new.html', {'form': form})

@require_POST
def posts_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:user_detail', request.user.id)

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:user_detail', request.user.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post':post })
