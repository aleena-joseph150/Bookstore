# Generated by Django 3.2.16 on 2023-01-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.IntegerField()),
                ('passw', models.CharField(max_length=20)),
                ('cpassw', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('utype', models.CharField(max_length=20)),
            ],
        ),
    ]