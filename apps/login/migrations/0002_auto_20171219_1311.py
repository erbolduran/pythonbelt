# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credit_card',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gallons',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
