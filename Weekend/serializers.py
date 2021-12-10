from rest_framework import serializers

from Weekend.models import UserFile


class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['title', 'html_file', 'code', 'data']
