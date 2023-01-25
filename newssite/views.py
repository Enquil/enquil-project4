from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from .models import Post, CATEGORY_CHOICES


def index(request):
    return render(request, 'index.html', {})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class CategoryList(generic.ListView):
    model = CATEGORY_CHOICES
    queryset = CATEGORY_CHOICES
