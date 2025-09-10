from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('bye/', views.bye, name='bye'),
    path('details/', views.teacher_details, name='teacher_details'),
]
