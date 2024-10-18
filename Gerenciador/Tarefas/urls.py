from django.urls import path
from . import views

urlpatterns = [
    path('api/tarefas/', views.task_list, name='tarefas-list'),
    path('api/tarefas/<int:id>/', views.task_detail, name='tarefas-detail'),
    path('api/tarefas/create/', views.task_create, name='ta-create'),
]
