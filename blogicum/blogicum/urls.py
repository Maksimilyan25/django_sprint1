from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),  # Главная страница
    path('pages/', include('pages.urls', namespace='pages')),  # Страницы
]
