from django.db import models

from author.models import User


class Article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, related_name='owner_article',
                               on_delete=models.CASCADE)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )

    def __str__(self):
        return self.title
