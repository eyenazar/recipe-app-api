from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successfull """
        email = 'testing@mail.ru'
        password = 'Testing12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@MAIL.ru'
        user = get_user_model().objects.create_user(email, 'testing12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testing12345')

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'testing@mail.ru',
            'testing12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
