from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    bio = models.TextField(max_length=500, blank = True, null=True)
    profile_pic = models.ImageField(upload_to = 'profile/', blank = True, null=True)
    contact = models.CharField(max_length = 10, blank = True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'projectImages/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
