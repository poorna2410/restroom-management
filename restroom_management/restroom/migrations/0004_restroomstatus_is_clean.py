# Generated by Django 5.1.3 on 2024-11-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroom', '0003_restroomstatus_cleaned_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restroomstatus',
            name='is_clean',
            field=models.BooleanField(default=True),
        ),
    ]
