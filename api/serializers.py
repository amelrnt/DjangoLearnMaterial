from rest_framework import serializers

from .models import Question, Question


class PollsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ('question_text')
