from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.
# this is function based view to  list all the posts.
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


# this is class based view to  list all the posts.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts' #By default django looks for a variable called "objectlist"
    template_name = "blog/home.html" #<app>/<model>_<viewtype>.html-> blog/post_list.html
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # We will follow strict django default  settings here, so we will not
    # Defuine context_object_name as we will use default "object" or "model name"
    # Defuine template_name as we will use default format that is blog/post_detail.html
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # We will follow strict django default  settings here, so we will not
    # Defuine context_object_name as we will use default "form" as it will be 
    # Used by both CreateView And UpdateView
    # Defuine template_name as we will use default format that is blog/post_form.html
    model = Post
    fields = ["title", "content"]
    #success_url = '/blog/'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # We will follow strict django default  settings here, so we will not
    # Defuine context_object_name as we will use default "form" as it will be 
    # Used by both CreateView And UpdateView
    # Defuine template_name as we will use default format that is blog/post_form.html
    model = Post
    fields = ["title", "content"]
    # success_url = '/blog/' instead of writing get_absolute_url in model we can use this one also

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False

class PoseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False





def about(request):
    return render(request, 'blog/about.html')