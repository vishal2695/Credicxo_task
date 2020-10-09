from rest_framework import serializers
from task1.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = "__all__"