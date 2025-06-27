from django.db import models
from django.contrib.auth.models import User

# Task model to represent a single to-do item
class Task(models.Model):
    # Links each task to a registered user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Short title of the task
    title = models.CharField(max_length=200, null=True, blank=True)

    # Optional detailed description
    description = models.TextField(null=True, blank=True)

    # Boolean flag for task completion
    complete = models.BooleanField(default=False)

    # Timestamp for when task was created
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # Display incomplete tasks first
        ordering = ['complete']
