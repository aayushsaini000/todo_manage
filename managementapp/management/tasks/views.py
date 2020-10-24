from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from tasks.models import Tasks
from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class CreateTasks(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            data = {
                "error": False,
                "msg": "Task Created"
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        tasks = Tasks.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def updatetask(self, request,task):
        try:
            task.task_name = request.data.get("task_name")
            task.description = request.data.get("description")
            task.created_at = request.data.get("created_at")
            task.start_date = request.data.get("start_date")
            task.end_date = request.data.get("end_date")
            task.status = request.data.get("status")
            task.save()
            return True
        except Exception:
            return False

    def put(self, request, format=None):
        taskid = request.GET.get("taskid")
        try:
            task = Tasks.objects.get(pk=taskid)
        except Exception:
            data = {
                "error": True,
                "msg": "No Task available with this id"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        taskStatus = self.updatetask(request,task)
        if taskStatus:
            data = {
                "error": False,
                "msg": "Task Updated"
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "error": True,
                "msg": "Somethings went wrong"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        taskid = request.GET.get("taskid")
        try:
            task = Tasks.objects.get(pk=taskid)
            task.delete()
        except Exception:
            data = {
                "error": True,
                "msg": "No Task available with this id"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "error": False,
            "msg": "Task deleted"
        }
        return Response(data, status=status.HTTP_200_OK)


