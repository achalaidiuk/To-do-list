from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todolist_project.forms import TaskCreationForm
from todolist_project.models import Task


@login_required()
def index(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()
    completed_tasks = all_tasks.filter(is_completed=True)
    incompleted_tasks = all_tasks.filter(is_completed=False)

    context = {
        "all_tasks_count": all_tasks.count(),
        "completed_tasks_count": completed_tasks.count(),
        "incompleted_tasks_count": incompleted_tasks.count(),
    }

    return render(request, "todolist_project/index.html", context)

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "create_task.html"
    success_url = reverse_lazy("todolist_project:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todolist_project:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist_project:task-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
