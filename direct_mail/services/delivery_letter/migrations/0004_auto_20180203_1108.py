# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 05:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audience', '0001_initial'),
        ('delivery_letter', '0003_letter_delivery_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='audience',
            field=models.ManyToManyField(to='audience.Audience'),
        ),
        migrations.AddField(
            model_name='letter',
            name='customer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
