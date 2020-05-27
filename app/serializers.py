from rest_framework.serializers import ModelSerializer
from app.models import *


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'text', 'author', 'date']