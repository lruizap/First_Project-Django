# Generated by Django 4.1.5 on 2023-01-20 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_taks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='taks',
            new_name='task',
        ),
    ]