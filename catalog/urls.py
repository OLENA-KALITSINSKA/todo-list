from django.urls import path
from .views import (
  HomePageView,
  TagListView,
  TaskCreateView,
  TagCreateView,
  TaskUpdateView,
  TaskDeleteView,
  TagUpdateView,
  TagDeleteView,
  ToggleTaskStatusView
)

urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("tags/", TagListView.as_view(), name="tag-list"),
  path("tasks/add/", TaskCreateView.as_view(), name="task-create"),
  path("tags/add/", TagCreateView.as_view(), name="tag-create"),
  path(
    "tasks/<int:pk>/update/",
    TaskUpdateView.as_view(),
    name="task-update"
  ),
  path(
    "tasks/<int:pk>/delete/",
    TaskDeleteView.as_view(),
    name="task-delete"
  ),
  path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
  path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
  path(
    "tasks/<int:pk>/toggle/",
    ToggleTaskStatusView.as_view(),
    name="toggle-task-status",
  ),
]

app_name = "catalog"
