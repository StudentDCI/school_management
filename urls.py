from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('details/', views.teacher_details)
]