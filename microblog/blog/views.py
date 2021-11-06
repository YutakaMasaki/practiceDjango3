from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView

from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model=Blog
    context_object_name = "blogs"
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    login_url = "/login"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    login_url = "/login"

    def get_success_url(self) -> str:
        blog_pk = self.kwargs["pk"]
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました")
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("index")
    login_url = "/login"

    def delete(self, form, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(form, *args, **kwargs)

