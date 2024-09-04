from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=14)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    author_image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    content = HTMLField()

    def __str__(self):
        return self.title + " by " + self.author

