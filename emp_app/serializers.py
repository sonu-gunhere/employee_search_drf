from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()
    department = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    company = serializers.CharField(required=False)