# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-17 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hetro_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='track',
            field=models.FileField(blank=True, null=True, upload_to='tracks'),
        ),
    ]
