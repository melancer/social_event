# Generated by Django 3.0.7 on 2020-07-05 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventing', '0009_auto_20200705_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='made_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 7, 5, 22, 21, 35, 469244), verbose_name='زمان ایجاد'),
            preserve_default=False,
        ),
    ]
