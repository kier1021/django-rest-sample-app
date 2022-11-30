from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    deleted_at = models.DateTimeField(blank = True, null=True)