# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bean_app', '0007_auto_20180210_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeebean',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]