from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']