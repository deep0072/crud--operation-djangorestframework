from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import NoteSerializer

from .models import Note

from rest_framework.response import Response

from rest_framework.decorators import api_view


@api_view(['GET'])
def getnotes(request):

    notes = Note.objects.all()

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getnote(request, pk):

    note = Note.objects.get(id=pk)
    print(note, "this is note")

    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(["POST"])
def create_note(request):

    data = request.data

    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def update_note(request, pk):

    data = request.data
    print(data, "this is the data")
    print(request.POST)

    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted")
