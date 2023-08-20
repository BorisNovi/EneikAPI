# Generated by Django 4.2.4 on 2023-08-19 13:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('header', models.CharField(max_length=255)),
                ('main_text', models.TextField(max_length=100000)),
                ('sub_text_0', models.TextField(max_length=50000)),
                ('images_0', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None)),
                ('sub_text_1', models.TextField(max_length=50000)),
                ('images_1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None)),
            ],
        ),
    ]
