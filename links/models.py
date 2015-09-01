from django.db import models

# Create your models here.
class Link(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    clicks = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)