# Generated by Django 3.2.4 on 2021-07-07 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210707_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='datecompleted',
        ),
    ]