from django.db import models

from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    creates = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")
