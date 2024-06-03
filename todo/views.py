from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import generics


class TodoListCreate(generics.ListCreateAPIView):
    queryset= Todo.objects.all()
    serializer_class= TodoSerializer

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Todo.objects.all()
    serializer_class= TodoSerializer






