from django.urls import path
from .views import *

urlpatterns = [
    path('', watch_content, name="watch_content"),
    path('options/', open_options, name="options"),
]