# # from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the tasks index.")

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

class TaskView(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  queryset = Task.objects.all()