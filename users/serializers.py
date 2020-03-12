from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    firstname = serializers.CharField(required=True, max_length=100)
    lastname = serializers.CharField(required=True, max_length=100)
    phone = serializers.CharField(required=True, max_length=20)
    email = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, write_only=True, min_length=5, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """

        user = User.objects.create(
            **validated_data,
            password=make_password(validated_data.pop("password")),
        )

        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """

        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.password = make_password(
            validated_data.get("password", instance.password)
        )
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ["firstname", "lastname", "phone", "email", "password"]


    def validate_email(self, value):
        list_users = User.objects.filter(email=value)

        if self.instance:
            list_users = list_users.exclude(pk=self.instance.pk)

        if list_users.exists():
            raise serializers.ValidationError("Email has been registered")
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone only numbers")
        return value
