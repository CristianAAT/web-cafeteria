# Generated by Django 2.2 on 2020-03-25 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200318_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 13, 10, 47, 665176, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]