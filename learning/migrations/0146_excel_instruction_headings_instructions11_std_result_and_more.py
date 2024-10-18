# Generated by Django 5.0.1 on 2024-03-11 11:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0145_compose_message_is_status_compose_message_read1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exel', models.FileField(blank=True, default=None, upload_to='pdf_files/')),
            ],
        ),
        migrations.CreateModel(
            name='instruction_headings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='instructions11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='std_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 11, 8, 54, 8392)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 11, 11, 8, 53, 989536)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 11, 11, 8, 53, 989536)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 11, 11, 8, 53, 989536)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 11, 11, 8, 53, 989536)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 3, 11, 11, 8, 53, 989536)),
        ),
        migrations.CreateModel(
            name='quiz_questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('choice1', models.CharField(max_length=100)),
                ('choice2', models.CharField(max_length=100)),
                ('choice3', models.CharField(max_length=100)),
                ('choice4', models.CharField(max_length=100)),
                ('is_correct', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.cls_name')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.subject')),
            ],
        ),
        migrations.CreateModel(
            name='set_timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houres', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('secondes', models.IntegerField()),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.cls_name')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.subject')),
            ],
        ),
    ]
