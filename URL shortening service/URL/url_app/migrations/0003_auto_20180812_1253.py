# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import url_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0002_auto_20180811_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=228, validators=[url_app.validators.validate_url, url_app.validators.validate_dot_com]),
        ),
    ]