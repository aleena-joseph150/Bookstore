# Generated by Django 3.2.16 on 2023-01-06 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_auto_20230106_1009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='publicmodel',
            new_name='storemodel',
        ),
    ]
