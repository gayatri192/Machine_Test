from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from datetime import datetime  # Import datetime module

from django.contrib.auth.models import User  # Assuming User model exists
from rest_framework.views import APIView

from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects = instance.project_set.all()
        project_serializer = ProjectSerializer(projects, many=True)
        data = serializer.data
        data['projects'] = project_serializer.data
        return Response(data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['updated_at'] = datetime.now()
        self.perform_update(serializer)
        return Response(serializer.data)





    @action(detail=True, methods=['post'])
    def projects(self, request, pk=None):
        client = get_object_or_404(Client, pk=pk)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project_name = serializer.validated_data.get('project_name')
            users_data = serializer.validated_data.get('users')

            # Add the client to the project
            project = serializer.save(client=client)

            # Assign already registered users to the project
            for user_data in users_data:
                user_id = user_data.get('id')
                user = get_object_or_404(User, pk=user_id)
                project.users.add(user)

            return Response(ProjectSerializer(project).data, status=201)
        return Response(serializer.errors, status=400)



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


