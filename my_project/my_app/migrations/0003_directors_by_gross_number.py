# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-10 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_directors_by_gross_directors_by_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='directors_by_gross',
            name='number',
            field=models.IntegerField(db_column='number', default=0),
        ),
    ]
