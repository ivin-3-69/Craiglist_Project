from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('search/', views.new_search, name ='new_search'),
]