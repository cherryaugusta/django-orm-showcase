from django.db import models
from django.utils import timezone


class PublishedCuisineManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            status="published",
            publish__lte=timezone.now()
        )

    def by_author(self, user):
        return self.get_queryset().filter(author=user)

    def search(self, keyword):
        return self.get_queryset().filter(
            name__icontains=keyword
        )
