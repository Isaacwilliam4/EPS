# Generated by Django 2.2 on 2020-07-29 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0004_auto_20200715_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipients', models.EmailField(max_length=254)),
                ('challenges', models.TextField()),
                ('help_to_give', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_reports', to='log_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pts', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_points', to='log_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('clock_in', models.DateTimeField()),
                ('clock_out', models.DateTimeField()),
                ('total_time', models.IntegerField()),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_days', to='log_reg_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='points',
            name='work_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='log_reg_app.Work_Day'),
        ),
        migrations.AddField(
            model_name='daily_report',
            name='work_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_report', to='log_reg_app.Work_Day'),
        ),
    ]
