from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    actors = models.CharField(max_length=30)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
