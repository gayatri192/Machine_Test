from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Project
        fields = '__all__'