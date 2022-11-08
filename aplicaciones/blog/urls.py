from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='index'),
    path('<slug:slug>/', post, name='detallep'),
    path('categorias/', categorias, name='categorias'),
    path('lista/', lista, name='lista'),
    path('prueba/', posst, name='prueba'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)