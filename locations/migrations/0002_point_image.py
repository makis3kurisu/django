# Generated by Django 5.1.4 on 2024-12-08 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='point_images/'),
        ),
    ]
