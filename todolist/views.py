import json
from django.shortcuts import render
from todolist.models import Task
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpRequest, HttpResponse, JsonResponse


def index(request:HttpRequest) -> HttpResponse:  
    title = "Daily to-do list"
    return render(request, "todolist/index.html",{
        'title': title,
        'n': Task.objects.all().count()
    })
   
@csrf_exempt
def tasks_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'tasks': [
                task.to_dict()
                for task in Task.objects.all()
            ]
        })
    if request.method == 'POST':
        var = False
        if 'completed' in request.POST:
            var = True

        task = Task.objects.create(
            priority = request.POST['priority_no'],
            task_name = request.POST['the_task'],
            time = request.POST['task_time'],
            # complete = var
        )
        return JsonResponse(task.to_dict())
    if request.method == "DELETE":
        Task.objects.filter(pk=int(request.body.decode("utf-8"))).delete()
        for task in Task.objects.all():
            print(task.to_dict())
        return JsonResponse({
            'task': [
                task.to_dict()
                for task in Task.objects.all()
            ]
        })
    if request.method == "PUT":
        data = request.body.decode('utf-8')
        request_json = json.loads(data)
        task = Task.objects.filter(pk=int(request_json['id']))
        task.update(name=request_json['name'])
        return JsonResponse({
            'task': [
                task.to_dict()
                for task in Task.objects.all()
            ]
        })