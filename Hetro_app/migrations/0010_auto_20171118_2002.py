# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hetro_app', '0009_auto_20171118_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
