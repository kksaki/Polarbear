# Generated by Django 4.1.2 on 2023-03-16 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bears', '0002_sighting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='temperature',
        ),
    ]