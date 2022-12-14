from django.contrib import admin

from .models import Question, Choice
# Register your models here.  

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)