
from rest_framework import serializers
from .models import Reminder

class RemindSeri(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'reminder_type']
