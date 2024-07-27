from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Tag, Task


class HomePageView(generic.ListView):
    model = Task
    template_name = "catalog/home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all()


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")
    template_name = "catalog/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")
    template_name = "catalog/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("catalog:home")
