# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('notification_type', models.IntegerField(choices=[(0, 'Introducing AVA'), (1, 'Invitation to join AVA'), (2, 'Update to your profile'), (3, 'Achievement Unlocked'), (4, 'Test Completed - Success!'), (5, 'Test Completed - Failure')], default=0, unique=True, verbose_name='Notification Type')),
                ('address_from', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=128)),
                ('body', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]