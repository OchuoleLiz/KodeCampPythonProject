from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True, max_length = 50)
    password = serializers.CharField(required = True, write_only = True, style = {'input_type': 'password'}, trim_whitespace = False)

    def  validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if Account.objects.filter(email = email).exists():
                user = authenticate(request = self.context.get('request'), email = email, password = password)
            else:
                message = {'detail': 'Invalid user credenbtials or user not registered', 'register': False}
                raise serializers.ValidationError(message)
            if not user:
                message = {'detail': 'Unable to log in with the provided credentials', 'register': True}
                raise serializers.ValidationError(message, code = 'authorization')
        else:
            message = 'Must provide "email" and "password"'
            raise serializers.ValidationError(message, code = 'authorization')
        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = ['id', 'email', 'is_active']

class RegistrationSerializer(RegisterSerializer):

    first_name = serializers.CharField(max_length=50, required=False)

    last_name = serializers.CharField(max_length=50, required=False)

    def validate_first_name(self, first_name):
        username = get_adapter().clean_username(first_name)
        return first_name

    def validate_last_name(self, last_name):
        username = get_adapter().clean_username(last_name)
        return last_name

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'first_name': self.validated_data.get('last_name', ''),
        }