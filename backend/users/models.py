from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import IndexedTimeStampedModel

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin site.")
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email


class Breed(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    temperament = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    description = models.TextField()
    life_span = models.CharField(max_length=255)

class Cat(models.Model):
    breeds = models.ManyToManyField(Breed)
    id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()

