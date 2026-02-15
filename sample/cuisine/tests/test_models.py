from django.test import TestCase
from django.contrib.auth.models import User
from cuisine.models import Cuisine


class CuisineModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="password"
        )

    def test_string_representation(self):
        cuisine = Cuisine.objects.create(
            name="Test Dish",
            slug="test-dish",
            desc="Description",
            author=self.user
        )
        self.assertEqual(str(cuisine), "Test Dish")
