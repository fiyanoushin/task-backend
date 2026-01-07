from rest_framework import serializers
from .models import CustomUser, Project

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "role")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ("created_by",)
