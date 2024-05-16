from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("task-list") #re-directing to the task view by using the name
    context = {"tasks":tasks}
    return render(request, "task_list.html", context)

def task_update(request):
    context = {}
    return render(request, "task_list.html", context)

def task_delete(request):
    context = {}
    return render(request, "task_delete.html", context)