# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20150831_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
