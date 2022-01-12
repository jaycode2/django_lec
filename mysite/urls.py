from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:content_id>/', views.detail, name='detail'),
]
