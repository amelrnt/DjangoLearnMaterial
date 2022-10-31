from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Choice, Question
from .serializers import PollsSerializer


class PollsApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request, *args, **kwargs):
    questions = Question.objects
    serializers = PollsSerializer(questions, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

class PollsDetailApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(request, question_id):
    try:
      return Choice.objects.filter(question=question_id)
    except Choice.DoesNotExist:
      return Response("data does not exist",status=status.HTTP_404_NOT_FOUND)
