from django.contrib import admin

from .models import MyUser, Post, Comment


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('get_username',)

    def has_change_permission(self, request, obj=None):
        return obj is not None and (
                request.user == obj.user
                or request.user.is_superuser
        )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

    def has_change_permission(self, request, obj=None):
        return obj is not None and (
                request.user == obj.author.user
                or request.user.is_superuser
        )

    def get_queryset(self, request):
        # Get the original queryset
        queryset = super().get_queryset(request)

        # Filter the queryset to exclude posts by blocked users
        blocked_by = request.user.myuser.blocked_by.all()
        queryset = queryset.exclude(author__in=blocked_by)

        return queryset


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')

    def has_delete_permission(self, request, obj=None):
        return obj is not None and (
                request.user == obj.author.user or
                request.user == obj.post.author.user or
                request.user.is_superuser
        )


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
