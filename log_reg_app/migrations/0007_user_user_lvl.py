# Generated by Django 2.2 on 2020-08-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0006_auto_20200729_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_lvl',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]