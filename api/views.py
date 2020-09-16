from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from classes.models import Classroom , Student
from .serializers import RegisterSerializer , ClassroomSerializer , ClassroomDetailsSerializer
from rest_framework.generics import ListAPIView

class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
