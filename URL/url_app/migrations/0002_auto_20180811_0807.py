# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=5, unique=True),
        ),
    ]
