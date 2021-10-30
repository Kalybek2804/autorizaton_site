from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.user.username
    
    def get_parent(self):
        return self.comment_user.filter(parent__isnull=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')

    def __str__(self):
        return self.user.username