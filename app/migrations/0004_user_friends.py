# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-18 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180518_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_friends_+', to='app.User'),
        ),
    ]