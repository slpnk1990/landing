from __future__ import unicode_literals
from distutils.command.upload import upload
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class HomePage(models.Model):
    key = models.CharField(max_length=150, db_index=True, unique=True)
    value = models.TextField(blank=True, max_length=500, db_index=True)
    link = models.CharField(max_length=80, db_index=True, unique=True)
    date_pub = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return '{}'.format(self.key)
        
class Menu(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    key = models.CharField(max_length=150, db_index=True, unique=True)
    link = models.CharField(max_length=80, db_index=True, unique=True)
    order = models.IntegerField(db_index=True, unique=True)
    date_pub = models.DateTimeField(auto_now=True)

class ImageAsset(models.Model):
    image = models.ImageField(upload_to='images')
    key = models.CharField(max_length=80, db_index=True, unique=True )
    date_pub = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=self.image.url,
            width=self.image.width,
            height=self.image.height
        ))

    image_tag.short_discription = 'Image Preview'

    def __str__(self):
        return '{}'.format(self.key)

class AboutUSModel(models.Model):
    key = models.CharField(max_length=150, db_index=True, unique=True)
    value = models.TextField(max_length=500, blank=True, db_index=True)
    link = models.CharField(max_length=80, db_index=True, unique=True)
    date_pub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.key)

class ContactSModel(models.Model):
    key = models.CharField(max_length=150, db_index=True, unique=True)
    value = models.TextField(max_length=500, blank=True, db_index=True)
    link = models.CharField(max_length=80, db_index=True, unique=True)
    date_pub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.key)