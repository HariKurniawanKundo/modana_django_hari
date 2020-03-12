import json
import unittest

from django.shortcuts import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User

# Create your tests here.

# initialize the APIClient app

class UsersListAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_list_users(self):
        response = self.factory.get(
            "/api/users/",
        )
        

class UsersCreateAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.first_payload = {
            "firstname": "Hari",
            "lastname": "",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.second_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.third_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "",
            "password": "ayam-goreng",
        }

        self.fourth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "",
        }

        self.fifth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam",
        }

        self.sixth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo",
            "password": "ayam-goreng",
        }

        self.seventh_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo",
            "password": "ayam-goreng",
        }

        self.eight_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "cobain",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.last_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "cobain",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

    def test_create_first_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.first_payload),
            format="json",
        )

    def test_create_second_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.second_payload),
            format="json",
        )

    def test_create_third_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.third_payload),
            format="json",
        )

    def test_create_fourth_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.fourth_payload),
            format="json",
        )

    def test_create_fifth_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.fifth_payload),
            format="json",
        )

    def test_create_sixth_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.sixth_payload),
            format="json",
        )

    def test_create_seventh_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.seventh_payload),
            format="json",
        )

    def test_create_eight_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.eight_payload),
            format="json",
        )

    def test_create_last_user(self):
        response = self.factory.post(
            "/api/users/",
            data=json.dumps(self.last_payload),
            format="json",
        )

class UsersUpdateAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user_object = User.objects.create(
            firstname= "Hari",
            lastname= "Kurniawan",
            phone= "08988005772",
            email= "hari.kurniawan.kundo@gmail.com",
            password= "ayam-goreng",
        )

        self.first_payload = {
            "firstname": "Hari",
            "lastname": "",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.second_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.third_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "",
            "password": "ayam-goreng",
        }

        self.fourth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "",
        }

        self.fifth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam",
        }

        self.sixth_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo",
            "password": "ayam-goreng",
        }

        self.seventh_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "08988005772",
            "email": "hari.kurniawan.kundo",
            "password": "ayam-goreng",
        }

        self.eight_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "cobain",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

        self.last_payload = {
            "firstname": "Hari",
            "lastname": "Kurniawan",
            "phone": "cobain",
            "email": "hari.kurniawan.kundo@gmail.com",
            "password": "ayam-goreng",
        }

    def test_update_first_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.first_payload),
            format="json",
        )

    def test_update_second_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users"+str(user.id)+"/",
            data=json.dumps(self.second_payload),
            format="json",
        )

    def test_update_third_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.third_payload),
            format="json",
        )

    def test_update_fourth_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.fourth_payload),
            format="json",
        )

    def test_update_fifth_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.fifth_payload),
            format="json",
        )

    def test_update_sixth_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.sixth_payload),
            format="json",
        )

    def test_update_seventh_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.seventh_payload),
            format="json",
        )

    def test_update_eight_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.eight_payload),
            format="json",
        )

    def test_update_last_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.put(
            "/api/users/"+str(user.id)+"/",
            data=json.dumps(self.last_payload),
            format="json",
        )

class UsersDeleteAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user_object = User.objects.create(
            firstname= "Hari",
            lastname= "Kurniawan",
            phone= "08988005772",
            email= "hari.kurniawan.kundo@gmail.com",
            password= "ayam-goreng",
        )

    def test_update_last_user(self):
        user = User.objects.get(pk=self.user_object.pk)
        request = self.factory.delete("/api/users/"+str(user.id)+"/")
