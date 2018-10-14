from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForms,NewTodoForm

def index(request):
    #form = TodoForms()
    newtodoform = NewTodoForm()
    todo_list = Todo.objects.order_by('id')
    context = {
        'todo_list': todo_list,
        'form': newtodoform
    }
    return render(request, 'todo/index.html', context)

@require_POST
def addtodo(request):
    #form = TodoForms(request.POST)

    newtodoform = NewTodoForm(request.POST)
    if newtodoform.is_valid():
       # new_todo = Todo(text=form.cleaned_data['text'])
       # new_todo.save()
        new_todo = newtodoform.save()

    return redirect('index')

def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
