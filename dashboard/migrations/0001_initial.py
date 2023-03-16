# Generated by Django 4.1.4 on 2023-03-15 11:00

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_url', models.URLField(validators=[dashboard.models.OptionalSchemeURLValidator])),
                ('site_status', models.IntegerField(default=404)),
                ('email', models.EmailField(max_length=50)),
                ('last_check_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
