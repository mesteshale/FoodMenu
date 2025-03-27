from django.urls import path
from . import views

app_name = 'group'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
]
