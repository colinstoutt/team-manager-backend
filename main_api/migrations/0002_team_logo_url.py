# Generated by Django 4.1 on 2023-02-19 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
