# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foursquare_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledata',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
