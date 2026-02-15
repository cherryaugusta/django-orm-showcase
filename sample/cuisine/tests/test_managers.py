from django.test import TestCase
from django.contrib.auth.models import User
from cuisine.models import Cuisine


class PublishedManagerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="password"
        )

        Cuisine.objects.create(
            name="Draft Dish",
            slug="draft-dish",
            desc="Draft",
            author=self.user,
            status="draft"
        )

        Cuisine.objects.create(
            name="Published Dish",
            slug="published-dish",
            desc="Published",
            author=self.user,
            status="published"
        )

    def test_published_manager(self):
        self.assertEqual(
            Cuisine.published.count(),
            1
        )
