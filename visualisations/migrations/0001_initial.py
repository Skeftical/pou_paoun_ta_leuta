# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeId', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField(null=True)),
                ('total', models.DecimalField(decimal_places=3, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='SubOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subOfficeId', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=3, max_digits=18)),
                ('pagio', models.DecimalField(decimal_places=3, max_digits=18)),
                ('taktikes', models.DecimalField(decimal_places=3, max_digits=18)),
                ('anaptuksiakes', models.DecimalField(decimal_places=3, max_digits=18)),
                ('approved', models.BooleanField()),
                ('revised', models.BooleanField()),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualisations.Office')),
            ],
        ),
    ]
