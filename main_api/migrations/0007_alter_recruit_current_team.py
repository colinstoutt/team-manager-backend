# Generated by Django 4.1 on 2023-02-19 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0006_recruit_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='current_team',
            field=models.CharField(max_length=100),
        ),
    ]