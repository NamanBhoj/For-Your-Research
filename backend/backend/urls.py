# myapp/urls.py
from django.urls import path
from fyr.views import run_spider

urlpatterns = [
    path('run_spider/', run_spider, name='run_spider'),
]
