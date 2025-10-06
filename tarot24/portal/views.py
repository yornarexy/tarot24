from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = '-time_publication'
    template_name = 'portal/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'portal/post_detail.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'portal/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_message'] = 'Добавить карту дня' if 'cart' in self.request.path else 'Добавить статью'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'article' in self.request.path:
            post.post_type = 'AR'
            post.save()
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'portal/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_message'] = 'Изменить карту дня' if 'cart' in self.request.path else 'Изменить статью'
        return context

class PostDelete(DeleteView):
    model = Post
    template_name = 'portal/post_delete.html'
    success_url = reverse_lazy('post_list')

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/post_edit.html'
