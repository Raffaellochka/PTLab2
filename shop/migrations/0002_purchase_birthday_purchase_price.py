# Generated by Django 4.1.5 on 2023-01-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
