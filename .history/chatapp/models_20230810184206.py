from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_lenght=100)
    sl
