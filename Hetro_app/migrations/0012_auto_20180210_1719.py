# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hetro_app', '0011_auto_20180209_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='procuder',
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(blank=True, default='Various', max_length=100),
        ),
    ]