from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=255)

    body = RichTextUploadingField()
    
    file = models.FileField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    tag = TaggableManager()
    creator = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True
    )
    
    class Meta:
        ordering = ['-create_date']


class Comment(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User,
        related_name='comment',
        on_delete=models.SET_NULL,
        null=True
    )


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        null=True
    )
    tag = TaggableManager()
