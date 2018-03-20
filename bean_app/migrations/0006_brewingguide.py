# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bean_app', '0005_auto_20180319_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2000)),
                ('steps', models.CharField(max_length=2000)),
                ('slug', models.SlugField(max_length=500, unique=True)),
            ],
        ),
    ]