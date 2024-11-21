from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('posts/<int:id>/', views.post_detail, name='post_detail'),  # Подробности поста
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),  # Публикации по категории
    path('category/<slug:category_slug>/', views.category_view, name='category_view'),
]