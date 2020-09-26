from rest_framework import serializers
from .models import *



class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')               


class UserSerializer(serializers.ModelSerializer):
    person_activity = ActivityPeriodSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'person_activity')
        


    
