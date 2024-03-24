from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job/<str:pk>', views.view_job, name = 'view_job'),
    path('create-post/', views.createPost, name="create-post"),
]