# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0003_auto_20180318_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='1', max_length=15)),
            ],
        ),
    ]