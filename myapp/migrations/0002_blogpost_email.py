# Generated by Django 4.2.11 on 2025-02-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
