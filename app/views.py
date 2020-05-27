from rest_framework.generics import *
from rest_framework.permissions import AllowAny
from app.models import *
from app.serializers import *


class NoteView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]