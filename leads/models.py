from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Lead(models.Model):
    SOURCE_CHOICES = (
        ("otr", "Other"),
        ("yt", "YouTube"),
        ("ggl", "Google"),
        ("nl", "NewsLetter"),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(18)]
    )

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=5, default="otr")
    profile_picture = models.ImageField(blank=True, null=True)
    special_file = models.FileField(blank=True, null=True)


class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(18)]
    )
