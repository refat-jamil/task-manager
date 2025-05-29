from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-task', views.task_list, name='my_task')

]
