from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(
        User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'MESSAGE'
        verbose_name_plural = 'MESSAGE'

    def __str__(self):
        return f"{self.author.username}"

    def last_30_messages(self):
        return Message.objects.order_by("-timestamp").all()[:10]
