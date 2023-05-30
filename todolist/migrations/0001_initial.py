# Generated by Django 4.1.2 on 2022-11-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('task_no', models.IntegerField(default=0)),
                ('time', models.DateTimeField(verbose_name='')),
            ],
        ),
    ]