# Generated by Django 4.2.1 on 2023-05-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_rename_user_name_tguser_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='user_first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user_last_name',
            field=models.CharField(max_length=50),
        ),
    ]
