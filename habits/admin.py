from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'time', 'place', 'user', 'is_pleasant', 'is_public')
    list_filter = ('is_pleasant', 'is_public', 'user')
    search_fields = ('action', 'place')
    