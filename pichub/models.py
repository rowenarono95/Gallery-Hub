# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Image(models.Model):
    name =models.CharField(max_length = 30)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    # image_category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to = 'images/', default='image.jpg')


class Location(models.Model):
    location_name = models.CharField(max_length = 30)
