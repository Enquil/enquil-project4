from . import views
from django.urls import path
import requests

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
]
