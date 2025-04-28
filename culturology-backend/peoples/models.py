from django.db import models

class People(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    photo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

