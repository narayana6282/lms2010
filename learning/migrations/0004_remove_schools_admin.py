# Generated by Django 4.2.5 on 2024-01-04 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_teachers_schools_homenav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schools',
            name='admin',
        ),
    ]
