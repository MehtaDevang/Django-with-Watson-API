# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180309_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000, null=True)),
                ('name', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]