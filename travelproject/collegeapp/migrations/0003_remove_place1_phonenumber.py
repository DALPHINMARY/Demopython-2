# Generated by Django 3.2.15 on 2022-10-04 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_place1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place1',
            name='phonenumber',
        ),
    ]
