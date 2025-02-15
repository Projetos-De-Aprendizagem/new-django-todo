from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, ListView, View
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm


class TodoListView(FormView, ListView):
    model = Todo
    template_name = 'todo_list.html'  # Custom template
    context_object_name = 'todos'  # Rename default "object_list"
    form_class = TodoForm
    success_url = reverse_lazy('todo-list')
    ordering = ['-id']  # Order tasks by newest first

    def form_valid(self, form):
        form.save()  # Salva a nova tarefa
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context

    
class ToggleTodoView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.is_done = not todo.is_done  # Toggle the status
        todo.save()
        return redirect('todo-list')

