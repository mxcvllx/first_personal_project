from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16, unique=True, null=True)
    profile_picture = models.ImageField(upload_to='prifile_picture/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return self.get_full_name()


class SocialAccount(models.Model):
    class ProviderTypes(models.TextChoices):
        GOOGLE = "google"
        FACEBOOK = "facebook"

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="social_account", null=True)
    social_account = models.CharField(max_length=50, choices=ProviderTypes.choices)
