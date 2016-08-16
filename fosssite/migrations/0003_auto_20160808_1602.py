# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fosssite', '0002_auto_20160804_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(blank=True, max_length=128)),
                ('about_me', models.TextField(blank=True)),
                ('twitterurl', models.URLField(blank=True)),
                ('facebookurl', models.URLField(blank=True)),
                ('lnkdnurl', models.URLField(blank=True)),
                ('githuburl', models.URLField(blank=True)),
                ('example', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='useredit',
            name='useredit',
        ),
        migrations.DeleteModel(
            name='UserEdit',
        ),
    ]
