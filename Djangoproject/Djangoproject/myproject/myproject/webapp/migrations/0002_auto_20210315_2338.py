# Generated by Django 3.1.3 on 2021-03-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timediff',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timediff',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
