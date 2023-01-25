from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from myapp.models import Project, task
from myapp.forms import CreateNewTask, CreateNewProjects

# Create your views here.


def index(request):
    title = '¡Django course!'
    return render(request, "index.html", {
        'title': title
    })


def helloWorld(request):
    return render(request, 'helloWorld.html')


def holaMundo(request, username):
    return HttpResponse(f'<h1>Hola {username}</h1>')


def projectsWeb(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/ProjectsWeb.html', {
        'projects': projects
    })


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def projects_Create(request):
    if request.method == 'GET':
        return render(request, 'projects/Projects_Create.html', {
            'forms': CreateNewProjects()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return render(request, 'projects/Projects_Create.html', {
            'forms': CreateNewProjects()
        })


def tasksWeb(request):
    tasks = task.objects.all()
    return render(request, 'tasks/TasksWeb.html', {
        'tasks': tasks
    })


def tasks(request, id):
    # tarea = task.objects.get(pk=id)
    tarea = get_object_or_404(task, pk=id)
    return HttpResponse(f'Tasks: {tarea.title}')


def tasks_Create(request):
    if request.method == 'GET':
        return render(request, 'tasks/Tasks_Create.html', {
            'form': CreateNewTask()
        })
    else:
        task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('Tareas Web')


def project_details(request, id):
    # project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = task.objects.filter(project_id=id)
    return render(request, 'projects/details.html', {
        'project': project.name,
        'tasks': tasks
    })
