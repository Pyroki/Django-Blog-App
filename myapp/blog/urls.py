from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path("post/<str:slug>", views.detail, name='detail'),
    # path("new_url", views.new_url, name='newurl'),
    # path("old_url", views.old_url_redirect, name='oldurl'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('new_post',views.new_post,name="new_post"),
    path('edit_post/<str:post_id>',views.edit_post,name="edit_post"),
    path('delete_post/<str:post_id>',views.delete_post,name="delete_post"),


]
