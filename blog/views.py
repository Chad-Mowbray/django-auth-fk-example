from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostCreateForm

class ListPostsView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "blog/all_posts.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/new.html"
    form_class = PostCreateForm
    success_url = "/blog/"

    def form_valid(self, form):
        ready_form = form.save(commit=False)
        ready_form.author = self.request.user
        return super().form_valid(form)
