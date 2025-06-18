from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-task', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:pk>', views.task_update, name='task-update'),
    path('delete/<int:pk>', views.task_delete, name='task-delete'),

    path('login/', views.login_view, name='login'),


]
