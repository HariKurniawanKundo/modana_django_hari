from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    firstname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    lastname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=20)
    email = serializers.CharField(required=False, allow_blank=True, max_length=150)
    password = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """

        user = User.objects.create(
            **validated_data, password=make_password(validated_data.pop("password")),
        )

        return user

    # def update(self, instance, validated_data):
    #     if "user" in validated_data:
    #         instance.user.password = make_password(
    #             validated_data.get("password", instance.user.password)
    #         )
    #         instance.user.save()

    class Meta:
        model = User
        fields = ["firstname", "lastname", "phone", "email", "password"]
