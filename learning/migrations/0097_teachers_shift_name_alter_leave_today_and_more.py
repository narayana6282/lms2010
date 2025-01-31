# Generated by Django 5.0.1 on 2024-02-07 14:26

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0096_alter_leave_today_alter_teachers_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='shift_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='learning.different_shifts'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 26, 24, 801805)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 7, 14, 26, 24, 776872)),
        ),
        migrations.CreateModel(
            name='Teacher_Shifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_off', models.CharField(max_length=100)),
                ('in_time', models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 26, 24, 777867))),
                ('late_mark_time', models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 26, 24, 777867))),
                ('out_time', models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 26, 24, 777867))),
                ('half_daytime', models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 26, 24, 777867))),
                ('facult_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.teachers')),
                ('shift_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.different_shifts')),
            ],
        ),
    ]
