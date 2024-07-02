from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.contrib import messages


# Create your views here.


def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo_items': todo_items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodoItem.objects.create(title=title, description=description)
        messages.success(request, 'Todo item added successfully!')
        return redirect('index')
    return render(request, 'todo/add_todo.html')

def mark_completed(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.completed = True
    messages.success(request, 'Todo item updated successfully!')
    todo_item.save()
    return redirect('index')

def view_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    return render(request, 'todo/view_todo.html', {'todo_item': todo_item})


def edit_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo_item.title = request.POST.get('title')
        todo_item.description = request.POST.get('description')
        todo_item.completed = 'completed' in request.POST
        todo_item.save()
        messages.success(request, 'Todo item updated successfully!')
        return redirect('index')
    return render(request, 'todo/edit_todo.html', {'todo_item': todo_item})


def delete_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo_item.delete()
        messages.success(request, 'Todo item deleted successfully!')
        return redirect('index')
    return render(request, 'todo/delete_todo.html', {'todo_item': todo_item})