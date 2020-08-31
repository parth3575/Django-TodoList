from . import views
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', views.task, name='task'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('status/<task_id>', views.status_task, name='task_status'),
]
