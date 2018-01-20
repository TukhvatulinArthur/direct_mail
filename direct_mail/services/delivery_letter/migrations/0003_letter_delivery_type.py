# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-20 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_letter', '0002_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='delivery_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='delivery_letter.DeliveryType'),
        ),
    ]
