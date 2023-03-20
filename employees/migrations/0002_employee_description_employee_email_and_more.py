# Generated by Django 4.1.3 on 2022-11-28 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_mvp',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
