from django.urls import path

from .views import *

urlpatterns = [
    path('', content, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')    
]