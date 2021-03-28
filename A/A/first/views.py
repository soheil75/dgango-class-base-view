from django.shortcuts import render
#from django.views import View
from django.views.generic.base import TemplateView
from .models import Todo

# class Home(View):
#     template_name = "first/home.html"
#     context = {'name':'Soheil'}
#     def get(self,request,*args,**kwargs):
#         return render (request,self.template_name,self.context)

class Home(TemplateView):
    template_name = "first/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context
    



