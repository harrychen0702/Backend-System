# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20180111_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='ave_gross',
            field=models.FloatField(db_column='ave_gross', default=0),
        ),
        migrations.AlterField(
            model_name='production',
            name='gross_box_office',
            field=models.FloatField(db_column='gross_box_office', default=0),
        ),
    ]
