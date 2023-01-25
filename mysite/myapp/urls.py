from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('helloWorld/', views.helloWorld, name='helloWorld'),
    path('hola/<str:username>', views.holaMundo, name='hola'),
    path('projects/', views.projects, name='proyectos'),
    path('projects/ProjectsWeb/<int:id>', views.project_details,
         name='Detalles del proyecto'),
    path('tasks/<int:id>', views.tasks, name='tarea'),
    path('projects/ProjectsWeb/', views.projectsWeb, name='Proyectos Web'),
    path('projects/Projects_Create/',
         views.projects_Create, name='Crear Proyecto'),
    path('tasks/TasksWeb/', views.tasksWeb, name='Tareas Web'),
    path('tasks/Tasks_Create/', views.tasks_Create, name='Crear Tarea'),
]
