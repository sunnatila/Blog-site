from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog, Comment


def home_page_view(request):
    return render(request, 'home.html')


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'new_blog.html'
    fields = ['author', 'title', 'summary', 'body', 'image']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'edit_blog.html'
    fields = ['title', 'summary', 'body', 'image']


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blogs')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['comment']

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.blog = Blog.objects.get(pk=pk)
        form.instance.author = self.request.user
        return super().form_valid(form)
