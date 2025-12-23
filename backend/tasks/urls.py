from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('tasks/add/', views.add_task),
    path('tasks/<int:id>/toggle/', views.toggle_task),
    path('tasks/<int:id>/delete/', views.delete_task),
]
