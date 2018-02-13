# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bean_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeproduct',
            name='average_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coffeeproduct',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='coffeeproduct',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='coffeeproduct',
            name='origin',
            field=models.CharField(max_length=128),
        ),
    ]