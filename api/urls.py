from django.urls import path

from . import views

app_name = "polls"
# with generic
urlpatterns = [
    path("", views.PollsApiView.as_view(), name="index"),
    path("<int:question_id>/", views.PollsDetailApiView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]