# Generated by Django 5.0.1 on 2024-01-11 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0031_delete_topics_alter_teachers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 11, 11, 40, 11, 486791)),
        ),
    ]