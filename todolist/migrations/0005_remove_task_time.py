# Generated by Django 4.0 on 2022-11-15 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_task_complete_alter_task_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
    ]