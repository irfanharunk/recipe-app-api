# Generated by Django 3.2.19 on 2023-05-18 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230518_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tags',
            new_name='tag',
        ),
    ]
