# Generated by Django 2.0.2 on 2018-02-06 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riskapp', '0002_auto_20180206_0652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='risk_fields',
            new_name='risk_field',
        ),
        migrations.RenameModel(
            old_name='risk_types',
            new_name='risk_type',
        ),
    ]
