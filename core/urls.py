from django.urls import path
from core.views import *

urlpatterns = [
    path('', homepage_view, name='homepage_view'),
    path('ApostaGerada/', generate_numbers, name='generate_numbers')
]