# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0005_compra_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
        migrations.AddField(
            model_name='post',
            name='compra',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lista.Compra'),
            preserve_default=False,
        ),
    ]
