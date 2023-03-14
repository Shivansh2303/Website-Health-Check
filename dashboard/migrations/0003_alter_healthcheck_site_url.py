# Generated by Django 4.1.4 on 2023-03-10 08:07

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_healthcheck_site_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcheck',
            name='site_url',
            field=models.URLField(max_length=25, validators=[dashboard.models.OptionalSchemeURLValidator]),
        ),
    ]
