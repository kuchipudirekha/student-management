from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile.png')

    def __str__(self):
        return self.full_name