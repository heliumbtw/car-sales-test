from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .test_json import test_json, test_json_put


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'username': 'car_dealer',
            'password': '12345'
        }
        response = self.client.post("/account/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TokenTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='car_dealer',
                                             password='12345')

    def test_token(self):
        data = {
            'username': 'car_dealer',
            'password': '12345'
        }
        response = self.client.post("/api-token-auth/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CarListTestCase(APITestCase):
    list_url = reverse('car-list')

    def setUp(self):
        self.user = User.objects.create_user(username='car_dealer',
                                             password='12345')
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()
        self.client.post(self.list_url, test_json, content_type='application/json')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_car_list_post_authenticated(self):
        response = self.client.post(self.list_url, test_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_car_list_post_un_test_car_list_post_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.list_url, test_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_car_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_car_list_delete_all_authenticated(self):
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_list_delete_all_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_car_list_delete_all_nothing_to_delete(self):
        self.client.delete(self.list_url)
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CarDetailTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='car_dealer',
                                             password='12345')
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()
        self.client.post(reverse('car-list'), test_json, content_type='application/json')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_car_detail_get_one_authenticated(self):
        response = self.client.get(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_detail_get_one_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_car_detail_update_one_authenticated(self):
        response = self.client.put(reverse('car-detail', kwargs={'pk': 1}),
                                   test_json_put, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_detail_update_one_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse('car-detail', kwargs={'pk': 1}),
                                   test_json_put, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_car_detail_delete_one_authenticated(self):
        response = self.client.delete(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_car_detail_delete_one_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse('car-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
