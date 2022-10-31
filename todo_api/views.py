from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
class TodoListApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(user=request.user.id)
        serializers = TodoSerializer(todos, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
            "user": request.user.id,
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        # get object from db
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    # get by id
    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
            "user": request.user.id,
        }
        serializer = TodoSerializer(
            instance=todo_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_200_OK,
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK,
        )
