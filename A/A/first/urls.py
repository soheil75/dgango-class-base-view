from django.urls import path
from . import views

app_name = 'first'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.TodoCreate.as_view(), name='create_todo'),
    path('<slug:myslug>', views.DetailTodo.as_view(), name='detail_todo'),
]
