from django.urls import path
from app1.views import *
app_name='morning'
urlpatterns=[
    path('goodmorning/',goodmorning,name='goodmorning'),
]