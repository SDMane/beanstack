# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bean_app', '0017_auto_20180301_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeebean',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='coffee_bean',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='bean_app.CoffeeBean'),
        ),
    ]