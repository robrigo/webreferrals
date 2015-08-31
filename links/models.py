from django.db import models

# Create your models here.
class Link(models.Model):
    slug = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)