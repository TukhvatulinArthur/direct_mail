# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 06:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_letter', '0005_letter_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
