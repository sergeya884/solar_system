from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_planets, name='all_planets'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('submit_leaderboard/', views.submit_leaderboard, name='submit_leaderboard'),
]
