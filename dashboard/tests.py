from django.test import TestCase
from django.urls import reverse


class DashboardAccessTests(TestCase):
    def test_dashboard_is_accessible_without_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data History')
        self.assertContains(response, 'Report')
        self.assertContains(response, 'Export Hari Ini')
        self.assertContains(response, 'Export 24 Jam')

    def test_login_and_register_routes_are_removed(self):
        self.assertEqual(self.client.get('/accounts/login/').status_code, 404)
        self.assertEqual(self.client.get('/accounts/register/').status_code, 404)
