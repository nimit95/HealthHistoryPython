# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhistory', '0003_auto_20170211_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
