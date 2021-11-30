from django.urls import path

from . import views
#Variable name helps Django distinguish this url.py file from
#files of the same name in other apps within the project
app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name = 'index'),
]