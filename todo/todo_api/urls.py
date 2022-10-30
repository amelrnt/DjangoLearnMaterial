from django.urls import include, path

from .views import TodoDetailApiView, TodoListApiView

urlpatterns = [
    path("api", TodoListApiView.as_view()),
    path("api/<int:todo_id>", TodoDetailApiView.as_view()),
]
