# Generated by Django 5.1.3 on 2024-11-10 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RestroomStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('entries', models.IntegerField(default=0)),
                ('exits', models.IntegerField(default=0)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('odour_level', models.IntegerField()),
                ('toiletries_stock', models.BooleanField(default=True)),
                ('restroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restroom.restroom')),
            ],
        ),
    ]
