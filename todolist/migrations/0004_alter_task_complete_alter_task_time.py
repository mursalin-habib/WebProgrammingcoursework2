# Generated by Django 4.0 on 2022-11-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_rename_task_no_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(verbose_name='%H:%M'),
        ),
    ]
