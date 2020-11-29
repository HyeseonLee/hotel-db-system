# Generated by Django 3.1.3 on 2020-11-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomApp', '0002_auto_20201117_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('STD', 'STANDARD'), ('SUP', 'SUPERIOR'), ('DEL', 'DELUXE'), ('EXC', 'EXECUTIVE'), ('STE', 'SUITE')], max_length=10),
        ),
    ]