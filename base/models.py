from django.db import models


class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    # participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
