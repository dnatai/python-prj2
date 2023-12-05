# Generated by Django 4.2.5 on 2023-10-30 07:57

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_gender_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(blank=True, default='cover.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
    ]
