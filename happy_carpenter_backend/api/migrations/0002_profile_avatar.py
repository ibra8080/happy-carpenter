# Generated by Django 5.0.7 on 2024-08-03 21:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar'),
        ),
    ]