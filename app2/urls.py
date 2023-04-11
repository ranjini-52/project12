from django.urls import path
from app2.views import *
app_name='evening'
urlpatterns=[
    path('goodevening/',goodevening,name='goodevening'),
]