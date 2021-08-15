# from django.shortcuts import render
from django.core.checks import messages
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import studentSerializer
from .models import Student
import json

# Create your views here.


def homepage(request):
    return HttpResponse("Welcome To API")


class studentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        data = json.loads(request.body)
        firstname = data.get('firstname', None)
        lastname = data.get('lastname', None)
        rollno = data.get('rollno', None)
        instance = Student.objects.create(
            firstname=firstname, lastname=lastname, rollno=rollno)
        instance.save()
        return Response(data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        student.firstname = data.get('firstname', None)
        student.lastname = data.get('lastname', None)
        student.rollno = data.get('rollno', None)
        student.save()
        return Response(studentSerializer(student).data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
