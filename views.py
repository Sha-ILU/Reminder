from rest_framework import generics
from .models import Reminder
from .serializers import RemindSeri

class RemindView(generics.CreateAPIView):
    query_set = Reminder.objects.all()
    serializer_class = RemindSeri
