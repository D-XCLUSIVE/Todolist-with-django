from django.shortcuts import render, redirect
from .models import Task



def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'tasks' : tasks,
    })

def completed(request):
    completed_task = Task.objects.filter(completed=True)
    return render(request, 'completed.html', {
        'completed' : completed_task, 
    })

def remaining(request):
     uncompleted_task = Task.objects.filter(completed=False)
     return render(request, 'remaining.html', {
        'remaining' : uncompleted_task, 
    })
    

def add_task(request):  
    if request.method == "POST":    
        title = request.POST.get('title') 
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')  
        completed = False 

        if title != "" and due_date != "" and due_time != "":
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time = due_time,
                completed=completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html')
    return render(request, 'add_task.html')

def delete_task(request):
    return render(request, 'delete.html')

def task_details(request):
    return render(request, 'task_detail.html')

