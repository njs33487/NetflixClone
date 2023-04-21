from django.db import models

from categories.models import Category

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField()
    video_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title
