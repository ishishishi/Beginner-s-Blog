from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    text = models.TextField()
    created_datetime = models.DateTimeField(default = timezone.now)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
