# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_remove_compra_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lista.Post'),
            preserve_default=False,
        ),
    ]
