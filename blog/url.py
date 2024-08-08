from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('ads/', ads, name='ads'),
    path('agro_industria/', agro_industria, name='agro_industria'),
    path('alimentos/', alimentos, name='alimentos'),
    path('apicultura/', apicultura, name='apicultura'),
    path('informatica/', informatica, name='informatica'),
    path('quimica/', quimica, name='quimica'),
]
