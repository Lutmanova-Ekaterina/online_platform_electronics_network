from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, )

    class Meta:
        model = User
        fields = ('email', 'password', )

    def create(self, validated_data):
        """переопределим, чтобы хешировался пароль"""
        return User.objects.create(username=validated_data['username'], password=make_password(validated_data['password']))
