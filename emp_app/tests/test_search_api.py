from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()

class TestEmployeeSearchTestCase(TestCase):
    
    def test_employee_search_valid_org(self):
        response = client.get('/api/search/', {'org_id': 'org1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_employee_search_with_filters(self):
        response = client.get('/api/search/', {
            'org_id': 'org1',
            'location': 'Mumbai',
            'status': 'Active'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for emp in response.data:
            self.assertEqual(emp['location'], 'Mumbai')
            self.assertEqual(emp['status'], 'Active')

    def test_employee_search_invalid_org(self):
        response = client.get('/api/search/', {'org_id': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_rate_limiting(self):
        for _ in range(10):
            client.get('/api/search/', {'org_id': 'org1'})
        response = client.get('/api/search/', {'org_id': 'org1'})
        self.assertEqual(response.status_code, 429)