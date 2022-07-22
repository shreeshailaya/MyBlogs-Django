from urllib import request
from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6,write_only=True)

    repeat_password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'repeat_password', 'first_name', 'last_name']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        password1 = attrs.get('password', '')
        password2 = attrs.get('repeat_password', '')

        if password1 != password2:
            raise serializers.ValidationError(
                'Password dont match'
            )

        if username.isalnum():
            raise serializers.ValidationError(
                'The username and Email is not same entered')
        return attrs

    def create(self, validated_data):
        validated_data.pop('repeat_password')
        return User.objects.create_user(**validated_data)
        

