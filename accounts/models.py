from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birthday = models.DateField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.username
