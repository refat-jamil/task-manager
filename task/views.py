from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForms


def home(request):
    return render(request, 'home.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'task_list':tasks}
    return render(request, 'task_list.html', context)

@login_required
def task_create(request):
    if request.method == "POST":
        task_form = TaskForms(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        task_form = TaskForms()

    context = {'task_form': task_form}

    return render(request, 'task_form.html', context)