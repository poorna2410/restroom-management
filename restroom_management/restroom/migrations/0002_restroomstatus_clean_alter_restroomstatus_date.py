# Generated by Django 5.1.3 on 2024-11-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restroomstatus',
            name='clean',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restroomstatus',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
