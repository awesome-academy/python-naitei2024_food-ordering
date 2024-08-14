from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu_view, name='menu'),
]
