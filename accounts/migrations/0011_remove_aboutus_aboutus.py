# Generated by Django 2.2.6 on 2021-04-25 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_aboutus_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='aboutus',
        ),
    ]
