from django.shortcuts import render
from rest_framework import serializers


from rest_framework.response import Response

from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from .models import *

from rest_framework.authentication import TokenAuthentication


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def home(request):
    permission_classes = [TokenAuthentication]
    student = Student.objects.all()
    json = StudentSerializer(student, many=True)
    return Response({'status': 200, "message": "successful", "data": json.data})
# Create your views here.


@api_view(["GET"])
def GetBook(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    # if serializer.is_valid():

    return Response({"status": 200, "message": "successful", "data": serializer.data})

    # return Response({"status": 403, "message": "not found"})


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
        return Response({'status': 403, "message": "something went wrong",  "error": serializer.errors})


@api_view(["PUT"])
def Update(request, id):

    try:

        student_obj = Student.objects.get(id=id)
        print(student_obj, "this is object")
        print(request.data)
        # set partial=True to update a data partially
        serializer = StudentSerializer(
            student_obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "successful", "data": serializer.data})

        return Response({"status": 403, "errors": serializer.errors})

    except Exception as e:
        return Response({"status": 403, "message": "invalid_id"})


# IN put method every field is need to be passed for updation of data
# while in  Patch  method only one field is passed for updation. we will pass an argument in response "partial = True"


@api_view(["DELETE"])
def Del_student(request, id):

    try:

        student_obj = Student.objects.get(id=id)
        print(request.data)
        # set partial=True to update a data partially
        student_obj.delete()

        return Response({"status": 200, "message": "deleted"})

    except Exception as e:
        return Response({"status": 403, "message": "invalid_id"})


# create
