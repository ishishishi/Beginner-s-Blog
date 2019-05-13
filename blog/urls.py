from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    path('', views.top, name='top'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('sign_out/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('posts/new/', views.posts_new, name='posts_new'),
    path('posts/<int:pk>/delete/', views.posts_delete, name='posts_delete'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
]
