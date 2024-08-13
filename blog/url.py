from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('ads/', ads, name='ads'),
    path('agro_industria/', agro_industria, name='agro_industria'),
    path('alimentos/', alimentos, name='alimentos'),
    path('apicultura/', apicultura, name='apicultura'),
    path('informatica/', informatica, name='informatica'),
    path('quimica/', quimica, name='quimica'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
