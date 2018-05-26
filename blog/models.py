from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10,
                              default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    published = PublishedManager()

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title
