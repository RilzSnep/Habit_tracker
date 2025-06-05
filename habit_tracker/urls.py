# habit_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('habits.urls')),  # Эта строка вызывает ошибку
    path('api/users/', include('users.urls')),  # Если у тебя есть приложение users
]
 
