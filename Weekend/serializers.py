from rest_framework import serializers

from Weekend.models import UserFile


class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['title', 'code', 'html_file']
