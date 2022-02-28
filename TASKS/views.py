from django.shortcuts import redirect, render
from .models import * 

from .forms import * 

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'tasks': tasks,  "form":form}
    return render(request, "TASKS/home.html", context)


def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, "TASKS/update.html", context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('home')

    context = {'task':task}
    return render(request, "TASKS/delete.html", context)