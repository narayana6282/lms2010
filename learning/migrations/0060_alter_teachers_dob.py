# Generated by Django 4.2.3 on 2024-02-02 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0059_rename_subject_description_stdclass_classid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 14, 1, 23, 791128)),
        ),
    ]