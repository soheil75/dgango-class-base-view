from django.shortcuts import render
#from django.views import View

from django.views.generic.base import TemplateView
from .models import Todo

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

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
    
class DetailTodo(DetailView):
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'

    def get_queryset(self,**kwargs):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['myslug'])
        else:
            return Todo.objects.none()

