# Generated by Django 2.2 on 2020-03-18 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200317_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 13, 35, 12, 745495, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]