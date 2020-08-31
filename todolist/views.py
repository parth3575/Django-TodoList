from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.http import HttpResponse


# Create your views here.
@login_required(login_url='user:login')
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
        messages.success(request, ("New task Added!"))
        return redirect('todolist:task')
    else:
        all_tasks = Task.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 3)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'task.html', {'all_tasks': all_tasks})
    # context_dict = {'welcome_task': 'Welcome to Task Page'}
    # return render(request, 'task.html', context=context_dict)


# @login_required(login_url='user:login')
def delete_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task_obj.delete()
        messages.success(request, ("Task is Deleted!"))
        return redirect('todolist:task')
    else:
        return render(request, 'delete.html', {'task_obj': task_obj})


@login_required(login_url='user:login')
def edit_task(request, task_id):
    if request.method == 'POST':
        task_obj = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))
        return redirect('todolist:task')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required(login_url='user:login')
def status_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    if task_obj.manage == request.user:
        task_obj.done = not task_obj.done
        task_obj.save()
    else:
        messages.success(request, ("Access Restricted!!!"))
    return redirect('todolist:task')


def index(request):
    context_dict = {'welcome_home': 'Welcome to MySite'}
    return render(request, 'index.html', context=context_dict)


def about(request):
    contact_form = ContactForm()
    context_dict = {'welcome_about': 'Welcome on About Page',
                    'contact_form': contact_form}
    return render(request, 'about.html', context=context_dict)