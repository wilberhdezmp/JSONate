# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import jsonate.fields
import test_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_withjsonatefieldexpectinglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelWithRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('many_to_many', models.ManyToManyField(related_name='many_to_my_model', to='test_app.MyModel')),
            ],
        ),
        migrations.AlterField(
            model_name='withjsonatefieldexpectinglist',
            name='some_json_data',
            field=jsonate.fields.JsonateField(default=[], validators=[test_app.models.validate_list]),
        ),
    ]
