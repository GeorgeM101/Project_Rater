from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='profpic/', default='default.jpeg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    bio = models.CharField(max_length=500)

    def save_profile(self):
        self.save()
    
    def __str__(self):
        return self.name
