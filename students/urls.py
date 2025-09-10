from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('bye/', views.bye, name='bye'),
    path('list/', views.student_list, name='student_list'),
    path('details/<int:pk>/', views.student_details, name='student_details'),
]
