from django.db import models
from django.utils import timezone

# Create your models here.
class ContactEntry(models.Model):
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message

