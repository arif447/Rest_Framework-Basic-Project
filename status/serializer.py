from rest_framework import serializers
from status.models import Status
# Serializer is kind of form in django ,
class status_serializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['pk', 'user', 'content', 'image']
