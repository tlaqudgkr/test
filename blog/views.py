from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from blog.models import BlogPost, GamePlay
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['play'] = GamePlay.objects.all()
        return context


class BlogDetailView(DetailView):
    model = BlogPost


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    template_name_suffix = '_update_form'


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['author', 'title', 'text', 'created_date', 'published_date']


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:bloglist')


class GameListView(ListView):
    model = GamePlay


class GameDetailView(TemplateView):
    template_name = 'blog/game_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        count_lt = GamePlay.objects.filter(usr=user, leftright="LT").count()
        count_rt = GamePlay.objects.filter(usr=user, leftright="RT").count()
        last_login = GamePlay.objects.filter(usr=user).order_by("-created_date")[0]
        context = super().get_context_data(**kwargs)
        context['user_id'] = user
        context['count_lt'] = count_lt
        context['count_rt'] = count_rt
        context['last_login'] = last_login
        return context