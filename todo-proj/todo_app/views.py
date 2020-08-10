from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TodoForm
from . import models
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView,
                                CreateView, DeleteView, UpdateView, View) 
from django.urls import reverse_lazy   
from django.contrib.auth.mixins import LoginRequiredMixin


###########################################################
########################## TODOS ##########################
###########################################################

# def home(request):
#     return render(request, "todo_app/home.html")

class HomeView(TemplateView):
    template_name = 'todo_app/home.html'

# @login_required
# def createtodo(request):
#     if request.method == "GET":
#         return render(request, "todo_app/createtodo.html", {'form':TodoForm()})
#     else:
#         try:
#             form = TodoForm(request.POST)
#             newtodo = form.save(commit=False)
#             newtodo.utente = request.user
#             newtodo.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, "todo_app/createtodo.html", {'form':TodoForm(), 'error':"Qualcosa e'andato storto. Riprova!"})

class CreateTodoView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'todo/viewtodo.html'
    model = models.Todo
    form_class = TodoForm
    # fields = ('titolo', 'memo', 'importante')   ##Use this or form_class##
    template_name = 'todo_app/createtodo.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.utente = self.request.user
        self.object.save()
        return super().form_valid(form)

# @login_required
# def viewtodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, utente=request.user)
#     if request.method == "GET":
#         form = TodoForm(instance=todo)
#         return render(request, "todo_app/viewtodo.html", {'todo':todo, 'form':form})
#     else:
#         try:
#             form = TodoForm(request.POST, instance=todo)
#             form.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, "todo_app/viewtodo.html", {'todo':todo, 'form':form,'error':"Ji fatt na cazzat. Arpruvc!"})

class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo
    template_name = "todo_app/viewtodo.html"

# def viewtodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, utente=request.user)
#     if request.method == "GET":
#         form = TodoForm(instance=todo)
#         return render(request, "todo_app/viewtodo.html", {'todo':todo, 'form':form})
#     else:
#         try:
#             form = TodoForm(request.POST, instance=todo)
#             form.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, "todo_app/viewtodo.html", {'todo':todo, 'form':form,'error':"Ji fatt na cazzat. Arpruvc!"})

# To retrieve the form prefilled use the GET method
class EditTodoView(LoginRequiredMixin,UpdateView):
    model = Todo
    form_class = TodoForm 
    template_name = "todo_app/edittodo.html"

# @login_required
# def currenttodos(request):
#     todos = Todo.objects.filter(utente=request.user, completato__isnull=True)
#     return render(request, "todo_app/currenttodos.html", {'todos':todos})

class CurrentTodosView(LoginRequiredMixin,ListView):
    context_object_name = 'todos'
    model = Todo
    template_name = 'todo_app/currenttodos.html'
    
    def get_queryset(self):
        return Todo.objects.filter(utente=self.request.user, completato__isnull=True) 

# @login_required
# def deletetodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, utente=request.user)
#     if request.method == "POST":
#         todo.delete()
#         return redirect('currenttodos')

# The DeleteView automatically looks for a template with the name of the model, all lower case,
# and appended _confirm_delete.html as a delete confirmation page, so if you want to implement
# it, set the first delete button as a GET request method, create todo_confirm_delete.html page
# and there in a form you can have the confirmation button (with a POST request method). 

class DeleteTodoView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('currenttodos') # go to the list of todos on successful deletion

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, utente=request.user)
    if request.method == "POST":
        todo.completato = timezone.now()
        todo.save()
        return redirect('currenttodos')

# @login_required
# def completedtodos(request):
#     todos = Todo.objects.filter(utente=request.user, completato__isnull=False).order_by('-completato')
#     return render(request, "todo_app/completedtodos.html", {'todos':todos})

class CompletedTodosView(LoginRequiredMixin,ListView):
    context_object_name = 'todos'
    model = models.Todo
    template_name = 'todo_app/completedtodos.html'

    def get_queryset(self):
        return Todo.objects.filter(utente=self.request.user, completato__isnull=False).order_by('-completato')   

### Authentication ###
class WelcomePage(TemplateView):
    template_name = 'todo_app/welcome.html'

class ThanksPage(TemplateView):
    template_name = 'todo_app/thanks.html'