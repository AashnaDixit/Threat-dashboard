# Generated by Django 5.1.3 on 2024-11-07 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_detected', models.DateField(default=datetime.date.today)),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
            ],
        ),
    ]
