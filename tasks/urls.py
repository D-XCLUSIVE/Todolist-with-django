from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed/', views.completed, name='done'),
    path('remaining', views.remaining, name='remaining'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('detail/<str:task_id>', views.task_details, name='task_detail'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='toggle_complete'),
]