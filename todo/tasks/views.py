from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *

# Home Page with Task Counter and Search
def index(request):
    search_query = request.GET.get('search', '')  # Get search query
    tasks = Task.objects.filter(title__icontains=search_query) if search_query else Task.objects.all()

    incomplete_tasks_count = tasks.filter(complete=False).count()  # Count incomplete tasks

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form, 'incomplete_tasks_count': incomplete_tasks_count}
    return render(request, 'tasks/list.html', context)


def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)  # Reusing update_task.html



# Task Update View
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

# Task Delete View
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
