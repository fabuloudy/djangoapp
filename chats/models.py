from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    login = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

class Chat(models.Model):
    user1 = models.ForeignKey(User,related_name = 'user1', on_delete = models.CASCADE,verbose_name = 'First User')
    user2 = models.ForeignKey(User,related_name = 'user2', on_delete = models.CASCADE,verbose_name = 'Second User')
    chatType = models.CharField(max_length=7,verbose_name = 'Chat Type')
