from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=200,
        unique=True
    )
    password = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.username


class CustomModel(models.Model):
    """Abstract model to add date to posts."""
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True


class Post(CustomModel):
    question = models.TextField(
        help_text='Enter your question'
    )
    answer = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='author'
    )

    class Meta:
        ordering = ['created']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.question[:10]
