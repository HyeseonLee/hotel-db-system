# Generated by Django 3.1.3 on 2020-11-25 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0003_request_roomservice_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]