# Generated by Django 3.1.5 on 2021-01-21 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210121_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categry',
            new_name='category',
        ),
    ]
