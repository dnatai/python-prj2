# Generated by Django 4.2.5 on 2023-11-02 06:03

from django.conf import settings
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_group_page_pagepost_grouppost'),
        ('userauths', '0005_alter_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='whatsapp',
        ),
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends_visibility',
            field=models.CharField(blank=True, choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='Everyone', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='groups', to='core.group'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pages',
            field=models.ManyToManyField(blank=True, related_name='pages', to='core.page'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, default='https://instagram.com/', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz123', length=7, max_length=25, prefix=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married')], default='single', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='working_at',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='whatsApp',
            field=models.CharField(blank=True, default='+123 (456) 789', max_length=100, null=True),
        ),
    ]
