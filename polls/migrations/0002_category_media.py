# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-19 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('idMedia', models.FloatField(primary_key=True, serialize=False)),
                ('mediaType', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=255)),
                ('created', models.BigIntegerField()),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=1500)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
        ),
    ]
