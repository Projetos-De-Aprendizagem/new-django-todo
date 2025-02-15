from django.contrib import admin
from django.urls import path
from .views import TodoListView, ToggleTodoView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('toggle-todo/<int:todo_id>/', ToggleTodoView.as_view(), name='toggle-todo'),
]