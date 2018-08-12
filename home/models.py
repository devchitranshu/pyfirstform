# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import sys
# Create your models here.


class FirstFormDB(models.Model):

   username = models.CharField(max_length = 50)
   filename = models.CharField(max_length = 50)
   message = models.CharField(max_length = 50)
   # phonenumber = models.IntegerField()

   class Meta:
      db_table = "firstformdb"

class FirstForm(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    csv = models.FileField(upload_to='csv')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
