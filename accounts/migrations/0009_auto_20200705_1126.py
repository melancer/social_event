# Generated by Django 3.0.7 on 2020-07-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200705_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.IntegerField(blank=True, choices=[(1, 'حقیقی'), (2, 'حقوقی')], null=True, verbose_name='نوع کاربری'),
        ),
    ]