# Generated by Django 2.2.1 on 2019-05-10 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rented_by',
        ),
    ]