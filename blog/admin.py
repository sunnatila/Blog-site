from django.contrib import admin
from .models import Blog, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

