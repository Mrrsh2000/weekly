from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from Weekend.serializers import *
from weekly.Responses import *


class UserViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = UserFile.objects.all()
        user = get_object_or_404(queryset, code=pk)
        serializer = UserFileSerializer(user)
        return SuccessResponse(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        queryset = UserFile.objects.filter(code=request.data['code'])
        if queryset.count() == 0:
            serializer = UserFileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return SuccessNotResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserFileSerializer(data=request.data)
            if serializer.is_valid():
                first = queryset.first()
                first.data = request.data['data']
                first.title = request.data['title']
                first.html_file = request.data['html_file']
                first.save()
                return SuccessResponse({
                    "code": first.code,
                    "data": first.data,
                    "title": first.title,
                    "html_file": first.html_file.url,
                }, status=status.HTTP_200_OK)
