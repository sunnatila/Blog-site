from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

class Blog(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, verbose_name='sarlavha')
    summary = models.CharField(max_length=500)
    body = RichTextField()
    image = models.ImageField(upload_to='blogs/images', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager

    def __str__(self):
        return f"{self.author} - {self.title}"

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.pk)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    at_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog} - {self.comment}"

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.blog.pk)])

