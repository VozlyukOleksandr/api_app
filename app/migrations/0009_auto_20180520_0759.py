# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-20 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_post_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='friends',
            field=models.ManyToManyField(default=None, null=True, related_name='_users_friends_+', to='app.Users'),
        ),
    ]
