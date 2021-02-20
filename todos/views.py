from django.shortcuts import render, redirect
from .forms import addForm
from .models import Todo


def add(request):
    form = addForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        is_completed = form.cleaned_data['is_completed']
        todo = Todo(title=title, description=description, is_completed=is_completed)
        todo.save()
        return redirect('/todos')
    return render(request, 'todos/add.html', {'form': form})