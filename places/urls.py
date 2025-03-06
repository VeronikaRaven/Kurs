from django.urls import path
from . import views

urlpatterns = [
    path('', views.places, name='places'),  # Главная страница приложения 
    path('<int:place_id>/', views.place_detail, name='place_detail'),
    path('<int:place_id>/add_review/', views.add_review, name='add_review'),
]


