from django.db import transaction
from .models import Cuisine


@transaction.atomic
def create_cuisine(**kwargs):
    return Cuisine.objects.create(**kwargs)


@transaction.atomic
def publish_cuisine(cuisine):
    cuisine.status = "published"
    cuisine.save()
    return cuisine
