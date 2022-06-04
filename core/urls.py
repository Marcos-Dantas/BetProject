from django.urls import path
from core.views import *

urlpatterns = [
    path('', homepage_view, name='homepage_view'),
    path('bilhete/', generate_ticket, name='generate_ticket')
]