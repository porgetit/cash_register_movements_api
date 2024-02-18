from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from apps.users.api.serializers import LoginSerializer

class LoginView (APIView) :
    def post(self, request) :
        serializer = LoginSerializer(data = request.data)
        
        if (serializer.is_valid()) :
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)
            
            if (user) :
                token, created = Token.objects.get_or_create(user = user)
                return Response({
                    'token': token.key,
                }, status = status.HTTP_200_OK)
            else :
                return Response({
                    'error': 'User or pass wrong',
                }, status = status.HTTP_400_BAD_REQUEST)
