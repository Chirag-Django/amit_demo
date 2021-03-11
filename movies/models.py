from django.db import models
from django.core import validators

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250, validators=[validators.MinLengthValidator(2)])
    actors = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[validators.MaxValueValidator(5),validators.MinValueValidator(1)])
    release_date = models.DateField()
    review = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
