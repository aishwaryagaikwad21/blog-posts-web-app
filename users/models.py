from django.db import models
from django.contrib.auth.models import User #defalut profile django provides

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #cascade if user is deleted then profile should be deleted
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'