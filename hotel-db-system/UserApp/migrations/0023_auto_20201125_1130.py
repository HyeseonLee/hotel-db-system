# Generated by Django 3.1.3 on 2020-11-25 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0022_auto_20201125_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='reseve_num',
            new_name='reserve_num',
        ),
    ]