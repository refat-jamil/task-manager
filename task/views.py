from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForms
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
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

@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    update_form = TaskForms(request.POST or None, instance=task)
    if update_form.is_valid():
        update_form.save()
        return redirect('task-list')
    context = {'update_form':update_form}
    return render(request, 'task_update.html', context)


def task_delete(request, pk):
    delete_task = Task.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        delete_task.delete()
        return redirect('task-list')
    return render(request, 'task_confirm_delete.html', {'task': delete_task})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
    return render(request, 'login.html')

