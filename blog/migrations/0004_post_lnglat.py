# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-04 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
