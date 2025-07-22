from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('applications/', views.applications, name='applications'),
    path('portfolio/', views.portfolio, name='portfolio'),
]