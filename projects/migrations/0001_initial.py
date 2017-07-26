# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40)),
                ('img_url', models.URLField(max_length=100)),
                ('repo_url', models.URLField(max_length=100)),
                ('project_url', models.URLField(max_length=100)),
                ('description_url', models.CharField(max_length=500)),
                ('technologies', models.CharField(max_length=100)),
            ],
        ),
    ]
