from django.db import models
from users.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    content = models.CharField(max_length = 180)
    created_at = models.DateTimeField(auto_now = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    deleted_at = models.DateTimeField(blank = True, null=True)

    def __str__(self):
        return self.content