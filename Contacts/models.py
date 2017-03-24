from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    photo = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return "{0} {1}".format (self.first_name, self.last_name)