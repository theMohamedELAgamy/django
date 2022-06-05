from contextlib import nullcontext
from email.policy import default
from django.db import models

from django.utils.translation import gettext_lazy as _


class Actor(models.Model):
  

    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    name = models.fields.CharField(verbose_name=_('Actor Name'), max_length=50)
    gender = models.fields.CharField(choices=GENDER, max_length=1, default='m')
    profile_image = models.ImageField(upload_to='actor',default='default.png')

    def __str__(self):
        return self.name
