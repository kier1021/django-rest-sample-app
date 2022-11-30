from rest_framework.views import APIView
from .serializers import CreateUserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status


class UserAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'username': request.data.get('username'),
            'is_superuser': False,
            'is_active': True,
            'is_staff': False,
        }
        
        serializer = CreateUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully created user', 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
