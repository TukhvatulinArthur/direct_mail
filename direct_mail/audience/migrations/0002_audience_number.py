# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audience',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]