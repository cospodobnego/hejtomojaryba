from django.urls import path
from .views import*

urlpatterns = [
    path('', BaseView.as_view()),
    path('game_2/', Game2View.as_view()),
]