from django.urls import path
from .views import *

urlpatterns = [
    path('', watch_content, name="watch_content"),
]