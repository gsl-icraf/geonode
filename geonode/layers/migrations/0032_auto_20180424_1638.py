# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 16:38
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0031_uploadsession_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfile',
            name='file',
            field=models.FileField(max_length=255, storage=django.core.files.storage.FileSystemStorage(base_url='/uploaded/'), upload_to='layers/%Y/%m/%d'),
        ),
    ]
