from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def tasks_page(request):
    """Render an HTML page listing all tasks from the database."""
    tasks = Task.objects.all().order_by('id')
    return render(request, 'tasks/list.html', {
        'tasks': tasks,
    })


def add_task(request):
    """Handle task creation via a simple POST form and redirect back to list."""
    if request.method == 'POST':
        text = (request.POST.get('text') or '').strip()
        if text:
            Task.objects.create(text=text)
    return redirect('tasks_list')


def delete_task(request, id):
    """Delete a task by id (POST) and redirect back to list."""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('tasks_list')


def mark_done(request, id):
    """Mark a task as completed (POST) and redirect back to list."""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        if not task.completed:
            task.completed = True
            task.save()
    return redirect('tasks_list')
