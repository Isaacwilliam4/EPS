# Generated by Django 2.2 on 2020-08-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0010_auto_20200803_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_day',
            name='clock_out',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM'),
        ),
    ]
