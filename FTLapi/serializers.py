from rest_framework import serializers
from FTLapp.models import *

## Serializer of the ActivityPeriod model
class ActivityPeriodSerializier(serializers.ModelSerializer):	

	class Meta:
		model=ActivityPeriod
		fields = ['start_time','end_time']

## Serializer of the User model
class UserSerializer(serializers.ModelSerializer):
	## Nesting the activity periods of the user along with his personal data
	activity_periods = ActivityPeriodSerializier(source='user_obj',many=True,read_only=True)
	
	class Meta:
		model=User
		fields = ['id','real_name','tz','activity_periods']

	