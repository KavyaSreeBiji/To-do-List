from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_page, name='tasks_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('done/<int:id>/', views.mark_done, name='mark_done'),
]
