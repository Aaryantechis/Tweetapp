# Generated by Django 3.2 on 2021-08-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
