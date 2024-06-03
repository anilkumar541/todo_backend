from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.TodoListCreate.as_view(), name="todo_list_create"),
    path("todos/<int:pk>/", views.TodoRetrieveUpdateDestroy.as_view(), name="todo_retrieve_update_destroy")
]

