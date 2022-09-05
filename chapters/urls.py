from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('chapter/<str:pk>/', views.chapter, name="chapter"),
    path('create-chapter/', views.create_chapter, name="create-chapter"),
    path('update-chapter/<str:pk>/', views.update_chapter, name="update-chapter"),
    path('delete-chapter/<str:pk>/', views.delete_chapter, name="delete-chapter"),

    path('create-picture/', views.create_picture, name="create-picture"),
    path('update-picture/<str:pk>/', views.update_picture, name="update-picture"),
    path('delete-picture/<str:pk>/', views.delete_picture, name="delete-picture"),
]