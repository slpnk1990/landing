from unicodedata import name
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(content), name='home'),
    path('about/', cache_page(60)(about), name='about'),
    path('contact/', cache_page(60)(contact), name='contacts'),
    
]