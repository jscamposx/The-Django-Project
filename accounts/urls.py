from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("signin/", views.signin_view, name = "signin"),
    path("admin_panel/", views.admin_panel, name = "admin_panel"),
    path("admin_panel/users", views.admin_panel_users, name = "admin_panel_users"),
    path("admin_panel/posts", views.admin_panel_posts, name = "admin_panel_posts"),
    path("admin_panel/contacts", views.admin_panel_contact, name = "admin_panel_contact"),
]
