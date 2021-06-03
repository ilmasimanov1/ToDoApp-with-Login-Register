from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
