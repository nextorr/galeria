# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Imagen(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    imageFile = models.ImageField(upload_to='images', null=True)

class ImageForm(ModelForm):
    class Meta:
        model = Imagen
        fields = {'url', 'title', 'description', 'type', 'imageFile'}


class Category(models.Model):
    name = models.CharField(max_length=255)

class Media(models.Model):
    idMedia = models.FloatField(primary_key=True)
    mediaType = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    created = models.BigIntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    url = models.CharField(max_length=1500)
    category = models.ForeignKey(Category, null=True)
