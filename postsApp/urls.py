from django.urls import path

from postsApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('add/post', views.add_post, name='add_post'),
    path('profile', views.profile, name='profile'),
    path('blockedUsers', views.blocked_users, name='blocked_users'),
    path('blockUser', views.block_user, name='block_user')
]
