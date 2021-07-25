from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

