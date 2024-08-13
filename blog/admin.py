from django.contrib import admin
from .models import Cursos

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ['nome']
