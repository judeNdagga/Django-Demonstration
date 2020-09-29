from .base_test import BaseTest


class RegisterUserTestCase(BaseTest):

    def test_register_user(self):
        """
        Test registering a user
        """
        url = f'{self.url}register/'
        response = self.client.post(url, data=self.user, format='json')
        self.assertEqual(response.status_code, 201)

    def test_register_invalid_user(self):
        """
        Register a user with invalid request body
        """
        url = f'{self.url}register/'
        response = self.client.post(url, data=self.invlaid_user, format='json')
        self.assertEqual(response.status_code, 400)

    def test_register_user_twice(self):
        """
        Test registering user with same username
        """
        url = f'{self.url}register/'
        response = self.client.post(url, data=self.user, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            url, data=self.user_username, format='json')
        self.assertEqual(response.status_code, 400)
