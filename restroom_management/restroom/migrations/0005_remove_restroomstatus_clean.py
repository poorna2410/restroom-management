# Generated by Django 5.1.3 on 2024-11-10 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restroom', '0004_restroomstatus_is_clean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restroomstatus',
            name='clean',
        ),
    ]
