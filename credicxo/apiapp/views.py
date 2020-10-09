from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task1.models import Student
from .serializers import StudentSerializers
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def studata(request):
    if request.method == 'GET':
        obj = Student.objects.all()
        serial = StudentSerializers(obj, many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = StudentSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def studatafind(request, id):
    try:
        obj = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serial = StudentSerializers(obj)
        return Response(serial.data)
    elif request.method == 'PUT':
        serial = StudentSerializers(obj, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        