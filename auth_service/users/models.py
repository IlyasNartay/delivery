# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Если хотим расширить поля, делаем так:
class CustomUser(AbstractUser):
    # Дополнительные поля, например телефон:
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
