from django.shortcuts import render
#from django.views import View

from django.views.generic.base import TemplateView
from .models import Todo

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import FormView
from .forms import TodoCreateForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages

from django.views.generic.edit import CreateView

from django.views.generic.edit import DeleteView

from django.views.generic.edit import UpdateView

from django.views.generic.dates import MonthArchiveView

from django.contrib.auth.mixins import LoginRequiredMixin

#from A.first import models

# class Home(View):
#     template_name = "first/home.html"
#     context = {'name':'Soheil'}
#     def get(self,request,*args,**kwargs):
#         return render (request,self.template_name,self.context)

# class Home(TemplateView):
#     template_name = "first/home.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["todos"] = Todo.objects.all()
#         return context


class Home(ListView):
    #model = Todo
    context_object_name = 'todos' #object_list
    template_name = 'first/home.html' #first/todo_list.html
    ordering = ['-created']
    #queryset = Todo.objects.all()
    def get_queryset(self):
        return Todo.objects.all()

#class DetailTodo(DetailView):
#     model = Todo
#     slug_field = 'slug'
#     slug_url_kwarg = 'myslug'
    
# class DetailTodo(DetailView):
#     slug_field = 'slug'
#     slug_url_kwarg = 'myslug'

#     def get_queryset(self,**kwargs):
#         if self.request.user.is_authenticated:
#             return Todo.objects.filter(slug=self.kwargs['myslug'])
#         else:
#             return Todo.objects.none()


class DetailTodo(LoginRequiredMixin,DetailView):
    model = Todo
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'

# class TodoCreate(FormView):
#     form_class = TodoCreateForm
#     template_name = 'first/todo_create.html'
#     success_url = reverse_lazy('first:home')

#     def form_valid(self,form):
#         self.create_todo(form.cleaned_data)
#         return super().form_valid(form)

#     def create_todo(self,data):
#         todo = Todo(title=data['title'],slug=slugify(data['title']))
#         todo.save()
#         messages.success(self.request,'your todo saved','success')

class TodoCreate(CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request,'your todo saved','success')
        return super().form_valid(form)

class DeleteTodo(DeleteView):
    model = Todo
    template_name = "first/todo_delete.html"
    success_url = reverse_lazy('first:home')

class UpdateTodo(UpdateView):
    model = Todo
    fields = ('title',)
    template_name = "first/todo_update.html"
    success_url = reverse_lazy('first:home')

class MonthTodo(MonthArchiveView):
    model = Todo
    date_field = 'created'
    month_format = '%m'
    template_name = 'first/todo_month.html'


