# Generated by Django 3.2.16 on 2023-01-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_rename_publicmodel_storemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('bprice', models.IntegerField()),
                ('des', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='bookapp/static/books')),
            ],
        ),
        migrations.CreateModel(
            name='contactmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('phn', models.IntegerField()),
                ('loc', models.CharField(max_length=50)),
            ],
        ),
    ]