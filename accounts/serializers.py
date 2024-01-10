# yourappname/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PanditProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PanditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanditProfile
        fields = '__all__'