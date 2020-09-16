from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime
from django.contrib.auth.models import User
from classes.models import Classroom , Student
from .serializers import RegisterSerializer , ClassroomSerializer , ClassroomDetailsSerializer,CreatClassroomSerializer
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

class ClassroomCreate(CreateAPIView):
    serializer_class = CreatClassroomSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreatClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
