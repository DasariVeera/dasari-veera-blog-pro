from django.urls import path
from django.shortcuts import render
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PoseDeleteView

urlpatterns = [
    path('blog/',PostListView.as_view(), name="home"),
    path('blog/<int:pk>/',PostDetailView.as_view(), name="detail"),
    path('blog/new/',PostCreateView.as_view(), name="create"),
    path('blog/<int:pk>/update/',PostUpdateView.as_view(), name="update"),
    path('blog/<int:pk>/delete/',PoseDeleteView.as_view(), name="delete"),
    path('about/',views.about, name="about")
]