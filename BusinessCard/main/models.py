from django.db import models

# Create your models here.
class ApplicationModel(models.Model):
    name = models.CharField(max_length=25)
    offer = models.TextField(max_length=600)
    email = models.EmailField()
    def __str__(self):
        return self.offer[:50]