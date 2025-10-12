from django.db import models
from django.urls import reverse

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='images/')  # uploads to MEDIA_ROOT/images/

    def __str__(self):
        return f"Message from {self.author} - {self.title}"