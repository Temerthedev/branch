from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

from account.serializers import UserRegistrationSerializer
import uuid

User = get_user_model()

from account.serializers import *


# Create your views here.

def get_tokens_for_user(user, password = None):
    refresh = RefreshToken.for_user(user)
    
    user = UserSerializer(user).data
    if password is not None:
        user['password'] = password

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': user
    }

def generate_password():
    return uuid.uuid4().hex[:10]

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        data = request.data

        if "email" not in data.keys():
            return Response({
                "error": "Email is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        if "password" not in data.keys():
            return Response({
                "error": "Password is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        email = data['email']
        password = data['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            user_id = User.objects.get(email=email)
            data = get_tokens_for_user(user_id)
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "User does not exist"
            }, status=status.HTTP_400_BAD_REQUEST)

# class UserRegistrationView(APIView):
#     # permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             data = get_tokens_for_user(user)
#             return Response(data, status=status.HTTP_201_CREATED)

#         # Creating dict with errors, keys are field names, values are error messages
#         errors = {}
#         for field, error_detail in serializer.errors.items():
#             errors[field] = error_detail[0]

#         return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)


class AdminRegistrationView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        
        user = request.user
        
        if not user.is_superadmin:
            return Response(
                    {'error': "You don't have a permission"},
                    status=status.HTTP_403_FORBIDDEN
            )
        
        # password = 
        # request.data['password'] = generate_password()
        
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = get_tokens_for_user(user)
            
            response_dict = {}
            response_dict['user'] = UserSerializer(user)
            response_dict.update(data)
            
            return Response(data, status=status.HTTP_201_CREATED)

        # Creating dict with errors, keys are field names, values are error messages
        errors = {}
        for field, error_detail in serializer.errors.items():
            errors[field] = error_detail[0]

        return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRegistrationView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        
        user = request.user
        
        if not user.is_superadmin or not user.is_admin:
            return Response(
                    {'error': "You don't have a permission"},
                    status=status.HTTP_403_FORBIDDEN
            )
        
        password_generated = generate_password()
        request.data['password'] = password_generated
        
        serializer = EmployeeRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = get_tokens_for_user(user, password_generated)
            
            
            return Response(data, status=status.HTTP_201_CREATED)

        # Creating dict with errors, keys are field names, values are error messages
        errors = {}
        for field, error_detail in serializer.errors.items():
            errors[field] = error_detail[0]

        return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)
