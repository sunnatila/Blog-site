from django.urls import path
from .views import (
    home_page_view,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/comment/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
]
