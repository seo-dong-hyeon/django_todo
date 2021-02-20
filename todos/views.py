from django.shortcuts import render
from .forms import addForm
from .models import Todo


def add(request):
    form = addForm(request.POST)
    form_title = 'Add Todo'
    confirm_message = None
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        is_completed = form.cleaned_data['is_completed']
        todo = Todo(title=title, description=description, is_completed=is_completed)
        todo.save()
        confirm_message = 'New Todo added'
        form = None
    return render(request, 'todos/add.html', {'form_title': form_title, 'form': form, 'confirm_message': confirm_message})