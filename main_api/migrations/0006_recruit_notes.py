# Generated by Django 4.1 on 2023-02-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0005_recruit_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='notes',
            field=models.TextField(default='', max_length=500),
        ),
    ]