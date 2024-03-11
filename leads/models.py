from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# User = get_user_model()
class User(AbstractUser):
	pass


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

	agent = models.ForeignKey('Agent', on_delete=models.RESTRICT)


class Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.RESTRICT)
	age = models.IntegerField(
		validators=[MaxValueValidator(100), MinValueValidator(18)]
	)
