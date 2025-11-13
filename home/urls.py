from django.urls import path, re_path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name='home'),
    re_path(r'^(?P<id>\d+)/upvote/$', views.upvote_post, name = "upvote_post"),
    re_path(r'^(?P<id>\d+)/delete_home/$', views.post_delete_home, name = "delete_home"),
]