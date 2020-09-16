from rest_framework import serializers
from django.contrib.auth.models import User

from classes.models import Classroom , Student
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'name', 'year', 'teacher']


class ClassroomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class CreatClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher',]
