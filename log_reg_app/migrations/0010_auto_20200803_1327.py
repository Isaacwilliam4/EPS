# Generated by Django 2.2 on 2020-08-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0009_auto_20200803_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_day',
            name='clock_out',
            field=models.DateTimeField(default=''),
        ),
    ]
