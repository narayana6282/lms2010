# Generated by Django 5.0.1 on 2024-02-07 14:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0109_teachers_shift_name_alter_leave_today_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 38, 18, 880141)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 38, 18, 856203)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 38, 18, 856203)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 38, 18, 856203)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 7, 14, 38, 18, 856203)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 7, 14, 38, 18, 855206)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='shift_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.different_shifts'),
        ),
    ]