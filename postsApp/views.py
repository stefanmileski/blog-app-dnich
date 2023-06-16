from django.shortcuts import render, redirect

from postsApp.forms import PostForm
from postsApp.models import Post, MyUser


def index(request):
    return render(request, 'postsApp/base.html')


def posts(request):
    user = request.user
    posts_list = Post.objects.exclude(author__user=user).exclude(author__in=user.myuser.blocked_by.all())
    return render(request, 'postsApp/posts.html', {
        'posts': posts_list
    })


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_to_add = form.save(commit=False)
            post_to_add.author = request.user.myuser
            post_to_add.save()
            return redirect('posts')
    return render(request, 'postsApp/add_post.html', {
        'form': form
    })


def profile(request):
    posts_list = Post.objects.filter(author__user=request.user)
    return render(request, 'postsApp/profile.html', {
        'posts': posts_list
    })


def blocked_users(request):
    blocked_users_list = request.user.myuser.blocked_users.all()
    users = MyUser.objects.exclude(user=request.user).exclude(user__myuser__in=request.user.myuser.blocked_users.all())
    return render(request, 'postsApp/blocked_users.html', {
        'blocked_users': blocked_users_list,
        'users': users
    })


def block_user(request):
    if request.method != 'POST':
        return None
    user_to_block = MyUser.objects.filter(user__username=request.POST.get('user_to_block'))[0]
    request.user.myuser.blocked_users.add(user_to_block)
    request.user.myuser.save()
    return redirect('blocked_users')
