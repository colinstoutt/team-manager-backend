# Generated by Django 4.1 on 2023-02-19 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0004_rename_team_name_team_mascot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('hometown', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('current_team', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruits', to='main_api.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('home_team', models.CharField(max_length=50)),
                ('away_team', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='main_api.team')),
            ],
        ),
    ]
