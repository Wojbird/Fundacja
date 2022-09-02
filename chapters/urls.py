from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('chapter/<str:pk>/', views.chapter, name="chapter"),
    path('create-chapter/', views.create_chapter, name="create-chapter"),
    path('update-chapter/<str:pk>/', views.update_chapter, name="update-chapter"),
    path('delete-chapter/<str:pk>/', views.delete_chapter, name="delete-chapter"),
]