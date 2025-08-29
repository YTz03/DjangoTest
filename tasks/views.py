from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
# Create your views here.
 
def update_tasks(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('title_'):
                task_id = key.split('_')[1]
                try:
                    task = Task.objects.get(id=task_id)
                    task.title = value
                    # עדכון הסטטוס
                    completed_key = f'completed_{task_id}'
                    task.completed = completed_key in request.POST
                    task.save()
                except Task.DoesNotExist:
                    pass
    return redirect('task_list')