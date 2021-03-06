# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_auto_20180111_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('rank', models.IntegerField(db_column='rank', primary_key=True, serialize=False)),
                ('actor', models.CharField(db_column='actor', default='NULL', max_length=100)),
                ('ave_rating', models.FloatField(db_column='ave_rating', default=0)),
                ('gross_box_office', models.FloatField(db_column='gross_box_office', default=0)),
                ('number', models.IntegerField(db_column='number', default=0)),
            ],
        ),
    ]
