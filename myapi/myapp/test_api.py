from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from myapp.models import Task

class UserTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user(self):
        url = reverse('login')
        User.objects.create_user(username='testuser', password='testpassword')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_logout_user(self):
        url = reverse('logout')
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)
        refresh = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'}, format='json').data['refresh']
        response = self.client.post(url, {'refresh': refresh}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.access_token = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'}, format='json').data['access']

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'title': 'Test Task', 'description': 'Test Description', 'user': self.user.id}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # Imprime los datos de respuesta para depurar
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        Task.objects.create(title='Test Task 1', description='Test Description 1', user=self.user)
        Task.objects.create(title='Test Task 2', description='Test Description 2', user=self.user)
        url = reverse('task-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)
        url = reverse('task-detail', args=[task.id])
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'user': self.user.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)
        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
