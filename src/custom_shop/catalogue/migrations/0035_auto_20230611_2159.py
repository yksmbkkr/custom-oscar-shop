# Generated by Django 3.2.19 on 2023-06-11 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0034_shoporder_cutoff_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoporder',
            name='cutoff_hour',
        ),
        migrations.AddField(
            model_name='category',
            name='cutoff_hour',
            field=models.PositiveIntegerField(default=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
        ),
    ]
