# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0003_auto_20170909_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('marca', models.TextField(blank=True, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='precio',
        ),
        migrations.AlterField(
            model_name='post',
            name='producto',
            field=models.ForeignKey(default=99999, on_delete=django.db.models.deletion.CASCADE, to='lista.Producto'),
            preserve_default=False,
        ),
    ]
