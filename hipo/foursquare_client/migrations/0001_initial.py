# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('search_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=70)),
                ('url', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('checkin_count', models.IntegerField()),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foursquare_client.History')),
            ],
        ),
    ]