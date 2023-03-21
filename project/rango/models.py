from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.TextField()
    author = models.TextField()
    date = models.TextField()
    news = models.TextField()
    def __str__(self):
        return self.title