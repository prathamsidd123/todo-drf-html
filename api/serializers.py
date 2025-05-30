from rest_framework import serializers
from .models import task_details

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = task_details
		fields ='__all__'