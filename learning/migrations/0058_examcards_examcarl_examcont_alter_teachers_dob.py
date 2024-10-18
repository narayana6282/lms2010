# Generated by Django 4.2.7 on 2024-02-01 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0057_alter_teachers_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='examcards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('field', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='examcarl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='examcont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 17, 35, 6, 914135)),
        ),
    ]