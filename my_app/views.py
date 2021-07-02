from django.shortcuts import render
from rest_framework import serializers


from rest_framework.response import Response

from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from .models import Student


@api_view(["GET"])
def home(request):
    student = Student.objects.all()
    json = StudentSerializer(student, many=True)
    return Response({'status': 200, "message": "successful", "data": json.data})
# Create your views here.


@api_view(["POST"])
def post_student(request):
    data = request.data
    print(data)

    serializer = StudentSerializer(data=data)

    if serializer.is_valid():

        serializer.save()
        return Response({'status': 200, "message": "successful", "data": serializer.data})
    else:
        print(serializer.data)
        return Response({'status': 403, "message": "something went wrong"})
