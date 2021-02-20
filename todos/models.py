from django.db import models
from datetime import datetime


class Todo(models.Model):
    # id
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    is_completed = models.BooleanField(default=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # id
    contents = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contents

