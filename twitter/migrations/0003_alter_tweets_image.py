# Generated by Django 3.2 on 2021-08-09 09:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_alter_tweets_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
