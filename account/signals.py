from django import dispatch
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile

@receiver(post_save, sender=User, dispatch_uid='THIS IS UNIQE')
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
