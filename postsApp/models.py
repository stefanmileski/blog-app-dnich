from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuser')
    blocked_users = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='blocked_by')
    full_name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='uploaded_files/', null=True, blank=True)
    interests = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    profession = models.CharField(max_length=100, blank=True)

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.get_username()


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to='uploaded_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
