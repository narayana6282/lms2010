# Generated by Django 5.0.1 on 2024-01-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('student_class', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('mobile_number', models.CharField(max_length=10)),
                ('parents_name', models.CharField(max_length=255)),
                ('parents_mobile_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]