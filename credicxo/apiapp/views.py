from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task1.models import Student
from .serializers import StudentSerializers
# Create your views here.

@api_view(['GET'])
def studata(request):
    if request.method == 'GET':
        obj = Student.objects.all()
        serial = StudentSerializers(obj, many=True)
        return Response(serial.data)