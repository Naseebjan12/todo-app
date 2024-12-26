from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks

# Create your views here.
def hello(request):
    if request.method == 'POST':
        title=request.POST['task']
        date=request.POST['date']
        description=request.POST['description']
        Tasks.objects.create(
            task_title=title,
            date=date,
            description=description
        )
        

        
        
        return render(request,'index.html')
    else:
        tasks=Tasks.objects.all()
        for task in tasks:
            print(task.title)
        return render(request,'index.html',tasks=tasks)