from rest_framework import status
from rest_framework.test import APITestCase


class CareerTestCase(APITestCase):

    def create_career(self, username='test'):
        data = {
            'username': username,
            'title': 'developer',
            'content': 'application test'
        }

        return self.client.post('/careers/', data, format='json')

    def test_create_career(self):
        response = self.create_career('daniel')

        self.assertEqual(response.data['username'], 'daniel')
        self.assertEqual(response.data['title'], 'developer')
        self.assertEqual(response.data['content'], 'application test')
        self.assertIsInstance(response.data['id'], int)
        self.assertIsInstance(response.data['created_datetime'], str)

    def test_cannot_create_career_when_invalid_data(self):
        response = self.client.post('/careers/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_paginated_careers(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['count'], 0)

        self.create_career('daniel')
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_cannot_update_username_id_created_datetime_when_using_patch(self):
        create_response = self.create_career('daniel')
        response = self.client.patch(f"/careers/{create_response.data['id']}/", {'username': 'updated', 'title': 'updated', 'content': 'updated'})

        self.assertEqual(response.data['username'], 'daniel')

    def test_delete_career(self):
        create_response = self.create_career('daniel')

        response = self.client.delete(f"/careers/{create_response.data['id']}/")
        self.assertEqual(response.data, {})