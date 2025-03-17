from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from auth_service.users.models import CustomUser

class AuthTestCase(APITestCase):

    def test_register_user(self):
        url = reverse('auth/register')  # Проверь, какой у тебя name у url
        data = {
            "email": "testuser@example.com",
            "password": "StrongPass123",
            "password2": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])

    def test_login_user(self):
        # Сначала регистрируем пользователя
        self.client.post(reverse('auth/register'), {
            "email": "testlogin@example.com",
            "password": "StrongPass123",
            "password2": "StrongPass123"
        }, format='json')

        # Теперь логинимся
        response = self.client.post(reverse('token_obtain_pair'), {
            "email": "testlogin@example.com",
            "password": "StrongPass123"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
