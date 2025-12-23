from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    data = [
        {
            "id": task.id,
            "text": task.text,
            "completed": task.completed
        }
        for task in tasks
    ]
    return Response(data)

@api_view(['POST'])
def add_task(request):
    text = request.data.get("text")
    if text:
        Task.objects.create(text=text)
    return Response({"status": "task added"})

@api_view(['PUT'])
def toggle_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return Response({"status": "updated"})

@api_view(['DELETE'])
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return Response({"status": "deleted"})
