from rest_framework.serializers import ModelSerializer
from .models import Application, Company, User
from rest_framework import serializers


class ApplicationSerializer(ModelSerializer):
    is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Application
        fields = ("__all__")


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("__all__")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        user = User(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user