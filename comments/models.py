from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='comments_comment', null=True, blank=True)

    def __str__(self):
        return self.text