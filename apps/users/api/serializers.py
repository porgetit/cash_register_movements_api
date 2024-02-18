from rest_framework import serializers
from django.contrib.auth.models import User

class LoginSerializer (serializers.Serializer) :
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer (serializers.Serializer) :
    class Meta :
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )