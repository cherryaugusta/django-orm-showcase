from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .managers import PublishedCuisineManager


STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)

TYPE_CHOICES = (
    ("veg", "Veg"),
    ("non veg", "Non Veg"),
)

CATG_CHOICES = (
    ("dessert", "Dessert"),
    ("snack", "Snack"),
    ("food", "Food"),
)


class Cuisine(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique_for_date="publish")
    desc = models.TextField()

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default="non veg",
    )

    catg = models.CharField(
        max_length=20,
        choices=CATG_CHOICES,
        default="food",
    )

    pic = models.ImageField(
        upload_to="cuisine/",
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        User,
        related_name="cuisine_posts",
        on_delete=models.CASCADE,
    )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
    )

    # Default manager
    objects = models.Manager()

    # Custom manager
    published = PublishedCuisineManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
            models.Index(fields=["status"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "cuisine:cuisine_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )
