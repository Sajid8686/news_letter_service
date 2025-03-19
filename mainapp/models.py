from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
