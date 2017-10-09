# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class History(models.Model):
    item = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    search_date = models.DateTimeField()

class TableData(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    venue_name = models.CharField(max_length=70)
    url = models.CharField(max_length=200) 
    phone_number = models.CharField(max_length=30)
    checkin_count = models.IntegerField()
