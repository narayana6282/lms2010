# Generated by Django 5.0.1 on 2024-02-06 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0086_cardpaymentfeatures_crpaymentfeatures_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admissioncards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='admissioncarl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='admissioncont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 9, 38, 39, 325943)),
        ),
    ]