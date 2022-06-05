from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Movie(models.Model):
    name = models.fields.CharField(verbose_name='Movie Name', max_length=50)
    director = models.ForeignKey('director',on_delete=models.CASCADE, null=True)

    production_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])

    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    actors = models.ManyToManyField('actor.actor')

    

    def __str__(self):
        return self.name
  
class Director(models.Model):
        name = models.fields.CharField(verbose_name='director Name', max_length=50)