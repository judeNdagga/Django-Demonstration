from rest_framework.test import APITestCase


class BaseTest(APITestCase):

    def setUp(self):
        self.url = '/auth/'

        self.user = {
            'username': 'Kengo',
            'email': 'kengo@email.com',
            'password': 'complex_password'
        }

        self.user_username = {
            'username': 'Kengo',
            'email': 'wada@email.com',
            'password': 'complex_password'
        }

        self.invlaid_user = {
            'username': 'Wada',
            'password': 'complex_password'
        }
