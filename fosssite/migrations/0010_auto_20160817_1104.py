# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fosssite', '0009_auto_20160817_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]