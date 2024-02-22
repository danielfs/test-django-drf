from django.db import models


class Career(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
