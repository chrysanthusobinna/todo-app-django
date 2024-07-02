from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.mark_completed, name='mark_completed'),
    
    path('view/<int:todo_id>/', views.view_todo, name='view_todo'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
