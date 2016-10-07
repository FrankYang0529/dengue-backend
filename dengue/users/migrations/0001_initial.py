# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_uuid', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='')),
                ('phone', models.TextField(default='')),
                ('is_signup', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
