# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToChandhkedaHD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('route', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ToChandhkedaWD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('route', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ToPalajHD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('route', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ToPalajWD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('route', models.CharField(max_length=100)),
            ],
        ),
    ]
