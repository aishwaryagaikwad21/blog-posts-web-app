from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
#one to many relationship.. bcz one user can have multiple posts but single post will have only one author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #if user is deleted then its post is also deleted

    def __str__(self):
        return self.title