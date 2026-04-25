from rest_framework import serializers
from .models import StudentRecord

class StudentRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord
        fields = '__all__'