from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'task_list':tasks}
    return render(request, 'task_list.html', context)