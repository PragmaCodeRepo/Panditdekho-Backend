# yourappname/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PanditProfile
from .serializers import PanditProfileSerializer
from rest_framework.authentication import TokenAuthentication


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user) 

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    



class PanditProfileListView(generics.ListCreateAPIView):
    queryset = PanditProfile.objects.all()
    serializer_class = PanditProfileSerializer
    permission_classes = [IsAuthenticated]

class PanditProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PanditProfile.objects.all()
    serializer_class = PanditProfileSerializer
    permission_classes = [IsAuthenticated]




class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Delete the user's authentication token
        request.auth.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)    