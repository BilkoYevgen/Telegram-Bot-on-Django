# Generated by Django 4.2.1 on 2023-05-22 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_task_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='TgUser',
        ),
    ]
